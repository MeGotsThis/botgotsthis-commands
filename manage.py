from lib.data import ManageBotArgs


async def manageNoCommand(args: ManageBotArgs) -> bool:
    if len(args.message) < 3:
        return False
    if args.message.lower[2] in ['list']:
        return True

    if len(args.message) < 4:
        return False
    if args.message.lower[2] in ['add', 'insert']:
        if await args.database.setChatProperty(
                args.message.lower[3], 'noCommandList', '1'):
            args.send('The !commands has been disabled for '
                      + args.message.lower[3])
        else:
            args.send('The !commands could not have been disabled for '
                      + args.message.lower[3] + '.')
        return True
    if args.message.lower[2] in ['del', 'delete', 'rem', 'remove', 'remove']:
        if await args.database.setChatProperty(
                args.message.lower[3], 'noCommandList'):
            args.send('The !commands has been enabled for '
                      + args.message.lower[3])
        else:
            args.send('The !commands could not have been enabled for '
                      + args.message.lower[3] + '.')
        return True
    return False
