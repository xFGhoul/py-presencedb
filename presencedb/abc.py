import os

from yarl import URL
from msgspec import Struct
from aiofile import async_open
from typing import Tuple, Dict, Self, TYPE_CHECKING

from .enums import ActivityID
from .utils import icon_to_bytes, humanize_iso_format, humanize_duration, HUMANIZE_DAYS
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
        return (
            cls(
                avatar_id=avatar_id,
                discord_id=discord_id,
                url=URL(f"{API.ICON}/{discord_id}/{avatar_id}"),
            )
            if discord_id != ActivityID.SPOTIFY
            else cls(avatar_id=avatar_id, discord_id=discord_id, url=API.SPOTIFY)
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
        avatar: BytesIO = await icon_to_bytes(self.url)
        async with async_open(path, "wb") as file:
            await file.write(avatar.read())


class TopUser:
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

    __slots__: Tuple[str, ...] = (
        "name",
        "discord_id",
        "avatar",
        "discriminator",
        "duration",
    )

    def __init__(self, data: Dict, format: bool) -> None:
        self.name: str = data.get("name")
        self.discord_id: int = data.get("dId")
        self.avatar: Avatar = Avatar._from_user(data.get("avatar"), self.discord_id)
        self.discriminator: str = data.get("discriminator")
        self.duration: int = (
            humanize_duration(data.get("duration"), HUMANIZE_DAYS)
            if format
            else data.get("duration")
        )

    def __repr__(self) -> str:
        return f"<TopUser name={self.name!r} duration={self.duration!r}>"


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

    __slots__: Tuple[str, ...] = (
        "date",
        "duration",
    )

    def __init__(self, data: Dict, format: bool) -> None:
        self.date: str = (
            humanize_iso_format(data.get("date")) if format else data.get("date")
        )
        self.duration: int = (
            humanize_duration(data.get("duration"), HUMANIZE_DAYS)
            if format
            else data.get("duration")
        )

    def __repr__(self) -> str:
        return f"<PlaytimeDate date={self.date!r} duration={self.duration!r}>"
