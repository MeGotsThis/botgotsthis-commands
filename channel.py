from datetime import timedelta

from lib.data import ChatCommandArgs
from lib.helper.chat import cooldown, permission, send

from . import library


@cooldown(timedelta(seconds=15), 'commands', 'moderator')
async def commandCommands(args: ChatCommandArgs) -> bool:
    if await args.data.getChatProperty(args.chat.channel, 'noCommandList'):
        return False

    return library.botCommands(args.chat.channel, send(args.chat))


@permission('broadcaster')
async def commandSetup(args: ChatCommandArgs) -> bool:
    return await library.botSetup(send(args.chat))
