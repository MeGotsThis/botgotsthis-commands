import configparser
import os
import urllib.parse
from typing import Optional

import aiofiles

from lib.data import Send


def botCommands(channel: Optional[str], send: Send) -> bool:
    msg: str = 'Command List: '
    if channel:
        msg += f'http://megotsthis.com/botgotsthis/t/{channel}'
    else:
        msg += 'http://megotsthis.com/botgotsthis/h/setup'
    send(msg)

    return True


async def botSetup(send: Send) -> bool:
    if os.path.isfile('twitchApi.ini'):
        ini = configparser.ConfigParser()
        async with aiofiles.open('twitchApi.ini', 'r',
                                 encoding='utf-8') as file:
            ini.read_string(await file.read(None))
    send(f'''\
Setup !status and !game: \
https://api.twitch.tv/kraken/oauth2/authorize?response_type=code\
&client_id={ini['twitch']['twitchClientID']}\
&redirect_uri={urllib.parse.quote_plus(ini['twitch']['redirectUri'])}\
&scope=channel_editor''')

    return True
