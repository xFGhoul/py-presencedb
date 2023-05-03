import os

from aiofile import async_open
from dataclasses import dataclass
from typing import Tuple, TYPE_CHECKING

from .utils import icon_to_bytes
from .constants import API

if TYPE_CHECKING:
    from io import BytesIO

__all__: Tuple[str, ...] = (
    "TopUser",
    "TopActivity",
    "TrendingActivity",
    "TopActivity",
)


@dataclass
class TopUser:
    """
    Class Representing A Top User

    Attributes
    ----------
    name: :class:`str`
        Name of User
    avatar: :class:`str`
        Avatar URL
    discriminator: :class:`str`
        User Discriminator
    dId: :class:`int`
        Discord ID of User
    duration: :class:`int`
        Duration User Has on Activity
    """

    name: str
    avatar: str
    discriminator: str
    dId: int
    duration: int

    def __post_init__(self):
        self.avatar = f"{API.AVATAR_BASE}/{self.dId}/{self.avatar}"

    async def save(self, path: os.PathLike) -> None:
        """Saves Current Activity To File

        Parameters
        ----------
        path : os.PathLike
            Path To Save File Too
        """
        bytes: BytesIO = await icon_to_bytes(self.avatar)
        async with async_open(path, "wb") as file:
            await file.write(bytes.read())


@dataclass
class TopActivity:
    """
    Class Representing A Top Activity

    Attributes
    ----------
    name: :class:`str`
        Name of Activity
    dId: :class:`int`
        ID of Activity
    icon: :class:`str`
        Activity Icon URL
    duration: :class:`int`
        Duration Activity Was Played For
    """

    name: str
    dId: int
    icon: str
    duration: int

    def __post_init__(self):
        self.icon = f"{API.ICON_BASE}/{self.dId}/{self.icon}"


@dataclass
class TrendingActivity:
    """
    Class Representing A Trending Activity

    Attributes
    ----------
    name: :class:`str`
        Name of Activity
    dId: class:`int`
        ID of Activity
    icon: :class:`str`
        Activity Icon URL
    duration: :class:`int`
        Duration Activity Has Been Played For
    """

    name: str
    dId: int
    icon: str
    duration: int

    def __post_init__(self):
        self.icon = f"{API.ICON_BASE}/{self.dId}/{self.icon}"


@dataclass
class PlaytimeDate:
    """
    Class Representing A Playtime Date

    Attributes
    ----------
    date: :class:`str`
        Date Activity Was Played On
    duration: :class:`int`
        Duration Activity Was Played For In Seconds
    """

    date: str
    duration: int
