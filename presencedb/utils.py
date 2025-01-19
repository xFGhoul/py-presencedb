import datetime
import io

from typing import Final, List, Optional, Tuple, Union

import aiohttp
import humanize

__all__: Tuple[str, ...] = (
    "icon_to_bytes",
    "humanize_duration",
)

HOURS: Final[str] = "hours"
DAYS: Final[str] = "days"


async def icon_to_bytes(icon: str) -> io.BytesIO:
    """
    Converts Icon URL To Bytes

    Args:
        icon (str): Icon URL

    Returns:
        io.BytesIO: Bytes like object of icon
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(icon) as response:
            return io.BytesIO(await response.read())


def _handle_duration_type(option: Union[HOURS, DAYS]) -> List[str]:
    """
    Handle the suppression of time units based on the duration type.
    
    Args:
        option (Union[HOURS, DAYS]): The duration type to handle. It can be either HOURS or DAYS.
    
    Returns:
        List[str]: A list of time units to suppress based on the given duration type.
    """
    
    suppress: List[str]
    if option == HOURS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif option == DAYS:
        suppress = [
            "seconds",
            "minutes",
            "seconds",
            "hours",
            "years",
            "months",
        ]
    return suppress


def humanize_duration(number: int, type: Optional[Union[HOURS, DAYS]] = HOURS) -> str:
    """Generates a Human Readable Duration

    Args:
        number (int): Duration To Format
        type (Optional[Union[HOURS, DAYS]]): If The Output Should Be Days or Hours, defaults to HOURS

    Returns:
        str: Humanized Duration
    """
    suppress = _handle_duration_type(type)
    duration: str = humanize.precisedelta(
        datetime.timedelta(seconds=number), suppress=suppress, format="%0.1f"
    )
    return duration


def humanize_iso_format(date: int, type: Optional[Union[HOURS, DAYS]] = DAYS) -> str:
    """
    Generatess a Human Readable Duration from ISO Format


    Args:
        date (int): Date That Needs To Be Formatted
        type (Optional[Union[HOURS, DAYS]]): If The Output Should Be Days or Hours, Defaults to DAYS

    Returns:
        str: Humanized Duration
    """
    suppress = _handle_duration_type(type)
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    seconds = (date - datetime.datetime(1970, 1, 1)).total_seconds()
    date: str = humanize.precisedelta(
        datetime.timedelta(seconds=seconds), suppress=suppress, format="%0.1f"
    )
    return date
