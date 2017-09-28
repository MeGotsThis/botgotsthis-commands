from typing import Mapping, Optional

from lib.data import ManageBotCommand

from .. import manage


def methods() -> Mapping[str, Optional[ManageBotCommand]]:
    if not hasattr(methods, 'methods'):
        setattr(methods, 'methods', {
            'nocommand': manage.manageNoCommand,
        })
    return getattr(methods, 'methods')
