import os

from yarl import URL
from msgspec import Struct
from aiofile import async_open
from typing import Tuple, Self, TYPE_CHECKING

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


class Avatar:
    """Class Representing an Avatar

    Attributes
    ----------
    id: :class:`str`
        ID of avatar
    url: :class:`str`
        URL of Avatar

    """

    __slots__: Tuple[str, ...] = (
        "avatar_id",
        "discord_id",
        "url",
    )

    def __init__(self, avatar_id: str, discord_id: str, url: str = "") -> None:
        self.avatar_id: str = avatar_id
        self.discord_id: str = discord_id
        self.url: URL = url

    def __repr__(self) -> str:
        return f"<Avatar url={self.url}>"

    def __eq__(self, other) -> bool:
        return self.avatar_id == other.avatar_id

    def __hash__(self) -> int:
        return hash(self.avatar_id)

    @classmethod
    def _from_activity(cls, avatar_id: str, discord_id: str) -> Self:
        return cls(
            avatar_id=avatar_id,
            discord_id=discord_id,
            url=URL(f"{API.ICON}/{discord_id}/{avatar_id}"),
        )

    @classmethod
    def _from_user(cls, avatar_id: str, discord_id: str) -> Self:
        return cls(
            avatar_id=avatar_id,
            discord_id=discord_id,
            url=URL(f"{API.AVATAR}/{discord_id}/{avatar_id}"),
        )

    @property
    def id(self) -> str:
        """Returns ID of Avatar

        Returns
        -------
        str
            Raw Avatar ID
        """
        return self.avatar_id

    async def save(self, path: os.PathLike) -> None:
        """Saves Current Avatar To File

        Parameters
        ----------
        path : os.PathLike
            Path To Save File Too
        """
        bytes: BytesIO = await icon_to_bytes(self.url)
        async with async_open(path, "wb") as file:
            await file.write(bytes.read())


class TopUser(Struct):
    """
    Class Representing A Top User

    Attributes
    ----------
    name: :class:`str`
        Name of User
    avatar: :class:`Avatar`
        User Avatar
    discriminator: :class:`str`
        User Discriminator
    dId: :class:`int`
        Discord ID of User
    duration: :class:`int`
        Duration User Has on Activity
    """

    name: str
    avatar: Avatar
    discriminator: str
    dId: int
    duration: int

    def __post_init__(self):
        self.avatar = Avatar._from_user(self.avatar, self.dId)


class TopActivity(Struct):
    """
    Class Representing A Top Activity

    Attributes
    ----------
    name: :class:`str`
        Name of Activity
    dId: :class:`int`
        ID of Activity
    icon: :class:`Avatar`
        Activity Icon
    duration: :class:`int`
        Duration Activity Was Played For
    """

    name: str
    dId: int
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<TopActivity name={self.name}>"


class TrendingActivity(Struct):
    """
    Class Representing A Trending Activity

    Attributes
    ----------
    name: :class:`str`
        Name of Activity
    dId: :class:`int`
        ID of Activity
    icon: :class:`str`
        Activity Icon URL
    duration: :class:`int`
        Duration Activity Has Been Played For
    """

    name: str
    dId: int
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<TrendingActivity name={self.name}>"


class PlaytimeDate(Struct):
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
