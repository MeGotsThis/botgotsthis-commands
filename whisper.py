from lib.data import WhisperCommandArgs
from lib.helper.whisper import send

from . import library


async def commandCommands(args: WhisperCommandArgs) -> bool:
    return library.botCommands(None, send(args.nick))


async def commandSetup(args: WhisperCommandArgs) -> bool:
    return await library.botSetup(send(args.nick))
