import io
import aiohttp
import humanize
import datetime

from typing import Union


async def icon_id_to_bytes(icon_id: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_id) as response:
            buffer = io.BytesIO(await response.read())
            return buffer


def humanize_duration(number: int, type: Union["hours", "days"]) -> int:
    if type == "hours":
        suppress = suppress = [
            "seconds",
            "minutes",
            "seconds",
            "days",
            "years",
            "months",
        ]
    elif type == "days":
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
