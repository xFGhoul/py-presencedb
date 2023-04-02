"""
                                                            _ _     
                                                           | | |    
  _ __  _   _   _ __  _ __ ___  ___  ___ _ __   ___ ___  __| | |__  
 | '_ \| | | | | '_ \| '__/ _ \/ __|/ _ \ '_ \ / __/ _ \/ _` | '_ \ 
 | |_) | |_| | | |_) | | |  __/\__ \  __/ | | | (_|  __/ (_| | |_) |
 | .__/ \__, | | .__/|_|  \___||___/\___|_| |_|\___\___|\__,_|_.__/ 
 | |     __/ | | |                                                  
 |_|    |___/  |_|                                                  

 Made With ❤️ By Ghoul
"""

import io
import aiohttp
import humanize
import datetime

from typing import Union, Optional, Final

HUMNANIZE_HOURS: Final[str] = "hours"
HUMANIZE_DAYS: Final[str] = "days"


async def icon_id_to_bytes(icon_id: str) -> io.BytesIO:
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_id) as response:
            buffer = io.BytesIO(await response.read())
            return buffer


def humanize_duration(number: int, type: Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]] = HUMNANIZE_HOURS) -> str:
    if type == HUMNANIZE_HOURS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif type == HUMANIZE_DAYS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "hours",
            "years",
            "months",
        ]

    duration = humanize.precisedelta(
        datetime.timedelta(seconds=number), suppress=suppress, format="%0.1f"
    )
    return duration
