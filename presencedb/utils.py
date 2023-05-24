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


def _handle_duration_type(option: Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]) -> List[str]:
    suppress: List[str]
    if option == HUMNANIZE_HOURS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif option == HUMANIZE_DAYS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "hours",
            "years",
            "months",
        ]
    return suppress


def humanize_duration(
    number: int, type: Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]] = HUMNANIZE_HOURS
) -> str:
    """Generates a Human Readable Duration

    Parameters
    ----------
    number: :class:`int`
        Duration To Format
    type: Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]]
        If The Output Should Be Days or Hours, defaults to HUMNANIZE_HOURS

    Returns
    -------
    str
        Humanized Duration
    """
    suppress = _handle_duration_type(type)
    duration: str = humanize.precisedelta(
        datetime.timedelta(seconds=number), suppress=suppress, format="%0.1f"
    )
    return duration


def humanize_iso_format(
    date: int, type: Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]] = HUMANIZE_DAYS
) -> str:
    """
    Generatess a Human Readable Duration from ISO Format


    Parameters
    ----------
    date: :class:`int`
        Date That Needs To Be Formatted
    type: :class:`Optional[Union[HUMNANIZE_HOURS, HUMANIZE_DAYS]]`
        If The Output Should Be Days or Hours, Defaults to HUMANIZE_DAYS

    Returns
    -------
    str
        Humanized Duration
    """
    suppress = _handle_duration_type(type)
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    seconds = (date - datetime.datetime(1970, 1, 1)).total_seconds()
    date: str = humanize.precisedelta(
        datetime.timedelta(seconds=seconds), suppress=suppress, format="%0.1f"
    )
    return date
