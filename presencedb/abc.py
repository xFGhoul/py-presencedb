import os
import msgspec

from yarl import URL
from msgspec import Struct
from aiofile import async_open
from typing import Tuple, Dict, Self, TYPE_CHECKING

from .enums import ActivityID
from .utils import icon_to_bytes, humanize_iso_format, humanize_duration, DAYS
from .constants import API

if TYPE_CHECKING:
    from io import BytesIO

__all__: Tuple[str, ...] = (
    "TopUser",
    "TopActivity",
    "UserTopActivity",
    "TrendingActivity",
    "UserTrendingActivity",
    "TopActivity",
)


class Avatar:
    """Avatar class for handling Discord user avatars.

    This class provides functionality to manage and interact with Discord user avatars,
    including fetching, saving, and accessing avatar metadata.

    Attributes:
        avatar_id (str): The unique identifier of the avatar.
        discord_id (str): The Discord ID of the user the avatar belongs to.
        url (str): The URL where the avatar image can be accessed.
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

        Returns:
            Raw Avatar ID
        """
        return self.avatar_id

    async def save(self, path: os.PathLike) -> None:
        """Saves Current Avatar To File

        Args:
            path: Path To Save File Too
        
        Returns:
            None
        
        Raises:
            IOError: If The File Cannot Be Written to Disk
        """
        avatar: BytesIO = await icon_to_bytes(self.url)
        async with async_open(path, "wb") as file:
            await file.write(avatar.read())


class TopUser:
    """
    Class representing a top user in PresenceDB.

    This class contains information about a user who ranks highly in an activity.

    Attributes:
        name (str): Name of the user.
        avatar (Avatar): User's avatar object.
        discriminator (str): User's Discord discriminator.
        dId (int): Discord ID of the user.
        duration (int): Duration the user has spent on the activity.
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
            humanize_duration(data.get("duration"), DAYS)
            if format
            else data.get("duration")
        )

    def __repr__(self) -> str:
        return f"<TopUser name={self.name!r} duration={self.duration!r}>"


class TopActivity(Struct):
    """
    Class representing a Top Activity on PresenceDB.

    Attributes:
        id (int): ID relating to PresenceDB.
        name (str): Name of the activity.
        dId (int): Discord ID of the activity.
        icon (Avatar): Activity's icon object.
        color (str): Color associated with the activity.
        added (str): Date when the activity was added.
        duration (int): Total duration the activity was played for.
    """

    id: int = msgspec.field(name="id")
    name: str
    dId: int
    color: str
    added: str
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<TopActivity name={self.name}>"


class UserTopActivity(Struct):
    """
    Class representing a user's Top Activity on Discord.

    Attributes:
        name (str): Name of the activity.
        dId (int): Discord ID of the activity.
        icon (Avatar): Activity's icon object.
        duration (int): Duration the activity was played for.
    """

    name: str
    dId: int
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<UserTopActivity name={self.name}>"


class TrendingActivity(Struct):
    """
    Class representing a Trending Activity on PresenceDB.

    Attributes:
        id (int): ID relating to PresenceDB.
        name (str): Name of the activity.
        dId (int): Discord ID of the activity.
        icon (Avatar): Activity Icon.
        added (str): Date activity was added.
        color (str): Color of the activity.
        duration (int): Duration activity has been played for.
    """

    id: int = msgspec.field(name="id")
    name: str
    dId: int
    added: str
    color: str
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<TrendingActivity name={self.name}>"


class UserTrendingActivity(Struct):
    """
    Class representing a User Trending Activity on PresenceDB.

    Attributes:
        name (str): Name of the activity.
        dId (int): Discord ID of the activity.
        icon (Avatar): Activity Icon.
        duration (int): Duration activity has been played for.
    """

    name: str
    dId: int
    icon: Avatar
    duration: int

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.icon, self.dId)

    def __repr__(self) -> str:
        return f"<UserTrendingActivity name={self.name}>"


class PlaytimeDate:
    """
    Class representing a playtime date record.

    Attributes:
        date (str): Date activity was played on.
        duration (int): Duration activity was played for.
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
            humanize_duration(data.get("duration"), DAYS)
            if format
            else data.get("duration")
        )

    def __repr__(self) -> str:
        return f"<PlaytimeDate date={self.date!r} duration={self.duration!r}>"
