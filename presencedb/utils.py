import io
import aiohttp
import humanize
import datetime

from typing import Union, Final

HUMNANIZE_HOURS: Final[str] = "hours"
HUMANIZE_DAYS: Final[str] = "days"


async def icon_id_to_bytes(icon_id: str) -> io.BytesIO:
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_id) as response:
            buffer = io.BytesIO(await response.read())
            return buffer


def humanize_duration(number: int, type: Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]) -> int:
    if type == HUMNANIZE_HOURS:
        suppress = suppress = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif type == HUMANIZE_DAYS:
        suppress = suppress = [
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
