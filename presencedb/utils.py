import datetime
import io

from typing import Final, List, Optional, Tuple, Union

import aiohttp
import humanize

__all__: Tuple[str, ...] = (
    "icon_to_bytes",
    "humanize_duration",
)

HUMNANIZE_HOURS: Final[str] = "hours"
HUMANIZE_DAYS: Final[str] = "days"


async def icon_to_bytes(icon: str) -> io.BytesIO:
    """Converts Icon URL To Bytes

    Parameters
    ----------
    icon : :class:`str`
        Icon URL

    Returns
    -------
    io.BytesIO
        Bytes Like Object Of Icon
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(icon) as response:
            return io.BytesIO(await response.read())


def humanize_duration(
    number: int, type: Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]] = HUMNANIZE_HOURS
) -> str:
    """Generates a Human Readable Duration

    Parameters
    ----------
    number : int
        Duration To Format
    type : Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]], optional
        If The Output Should Be Days or Hours, defaults to HUMNANIZE_HOURS

    Returns
    -------
    str
        Humanized Duration
    """
    if type == HUMNANIZE_HOURS:
        suppress: List[str] = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif type == HUMANIZE_DAYS:
        suppress: List[str] = [
            "seconds",
            "minutes",
            "seconds",
            "hours",
            "years",
            "months",
        ]

    duration: str = humanize.precisedelta(
        datetime.timedelta(seconds=number), suppress=suppress, format="%0.1f"
    )
    return duration
