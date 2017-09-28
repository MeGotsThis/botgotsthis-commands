from typing import Mapping, Optional

from lib.data import WhisperCommand

from .. import whisper


def commands() -> Mapping[str, Optional[WhisperCommand]]:
    if not hasattr(commands, 'commands'):
        setattr(commands, 'commands', {
            '!commands': whisper.commandCommands,
            '!setup': whisper.commandSetup,
        })
    return getattr(commands, 'commands')


def commandsStartWith() -> Mapping[str, Optional[WhisperCommand]]:
    return {}
