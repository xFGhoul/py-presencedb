from msgspec import Struct
from typing import Dict, List, Tuple

from .abc import PlaytimeDate, UserTopActivity, UserTrendingActivity, Avatar
from .utils import (
    DAYS,
    HOURS,
    humanize_duration,
    humanize_iso_format,
)

__all__: Tuple[str, ...] = (
    "User",
    "UserStats",
)


class User:
    """
    Class Interface Containing User Attributes

    Attributes:
        id (int): PresenceDB internal user ID.
        discord_id (int): User Discord ID.
        name (str): User's name.
        discriminator (str): User's Discord discriminator.
        inactive (str): Returns a date of when the user became inactive.
        added (str): Date user's account was added.
        color (str): Color of user's account.
        avatar (Avatar): User avatar.
        plus (bool): If the user has subscribed to PresenceDB Plus.
        tracker (Dict): Information about current user activity.
        timestamp (str): Timestamp of current activity.
        current_activities (List[CurrentActivity]): List of current user activities.
        stats (UserStats): Object representing user statistics.
        tag (str): Combination of self.name + self.discriminator.
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "discord_id",
        "name",
        "discriminator",
        "inactive",
        "private",
        "added",
        "color",
        "avatar",
        "plus",
        "tracker",
        "timestamp",
        "current_activities",
        "stats",
        "tag",
    )

    def __init__(
        self, data: Dict, stats: Dict, trending: Dict, top: Dict, format: bool
    ) -> None:
        self.id: int = data.get("id")
        self.discord_id: int = data.get("dId")
        self.name: str = data.get("name")
        self.discriminator: str = data.get("discriminator")
        self.inactive: str = data.get("inactiveSince")
        self.private: bool = data.get("private")
        self.added: str = (
            humanize_iso_format(data.get("added")) if format else data.get("added")
        )
        self.color: str = data.get("color")
        self.avatar: Avatar = Avatar._from_user(data.get("avatar"), self.discord_id)
        self.plus: bool = data.get("plus")
        self.tracker: Dict | None = data.get("tracker")
        self.timestamp: str | None = (
            self.tracker.get("timestamp") if self.tracker else None
        )
        self.current_activities: CurrentActivity | None = (
            [CurrentActivity(**activity) for activity in self.tracker.get("activities")]
            if self.tracker
            else None
        )
        self.stats: UserStats = UserStats(stats, trending, top, format)
        self.tag: str = f"{self.name}#{self.discriminator}"

    def __repr__(self):
        return f"<User tag={self.tag!r}>"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


class UserStats:
    """
    Class Interface Representing Stats of a User

    Attributes:
        total_duration (str): Total Duration of Activity Recorded
        trending_duration (int): Trending Duration of Activities
        top_users (List[TopUser]): List of Top Users For The Activity
        playtime_dates (List[PlaytimeDate]): List of Playtime Dates For Activity
        top_activities (List[TopActivity]): List of Top Activities For User
        trending_activities (List[TrendingActivity]): List of Trending Activities For User
        avatar_history (List[AvatarHistory]): List of Avatars Users Recorded
    """

    __slots__: Tuple[str, ...] = (
        "total_duration",
        "trending_duration",
        "playtime_dates",
        "top_activities",
        "trending_activities",
        "avatar_history",
        "records",
    )

    def __init__(self, stats: Dict, trending: Dict, top: Dict, format: bool) -> None:
        self.total_duration: str = (
            humanize_duration(stats.get("totalDuration"), DAYS)
            if format
            else stats.get("totalDuration")
        )
        self.trending_duration: int = (
            humanize_duration(stats.get("trendingDuration"), HOURS)
            if format
            else stats.get("trendingDuration")
        )
        self.playtime_dates: List[PlaytimeDate] = [
            PlaytimeDate(date, format) for date in stats.get("playtimeDates")
        ]
        self.top_activities: List[UserTopActivity] = [
            UserTopActivity(**activity) for activity in top
        ]
        self.trending_activities: List[UserTrendingActivity | None] = (
            [UserTrendingActivity(**activity) for activity in trending]
            if trending
            else None
        )
        self.avatar_history: List[AvatarHistory] = [
            AvatarHistory(avatar, format) for avatar in stats.get("avatarHistory")
        ]
        self.records: List[Record] = [
            Record(record, format) for record in stats.get("records")
        ]

    def __repr__(self) -> str:
        return f"<UserStats total_duration={self.total_duration!r}>"


class CurrentActivity(Struct):
    """
    Class Representing A Current Activity

    Attributes:
        name (str): Name of Activity
        id (int): ID of Activity
    """

    name: str
    id: int


class AvatarHistory:
    """
    Class Representing A User's Avatar History

    Attributes:
        id (int): ID of Avatar
        discord_id (int): Discord ID Pertaining to Avatar
        avatar (Avatar): Avatar
        added (str): Date Avatar Was Added
        hidden (bool): Whether Avatar Is Hidden From Site
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "discord_id",
        "avatar",
        "added",
        "hidden",
    )

    def __init__(self, data: Dict, format: bool) -> None:
        self.id: int = data.get("id")
        self.discord_id: int = data.get("dUserId")
        self.avatar: Avatar = Avatar._from_user(data.get("avatar"), self.discord_id)
        self.added: str = (
            humanize_iso_format(data.get("added")) if format else data.get("added")
        )
        self.hidden: bool = data.get("hidden")

    def __repr__(self) -> str:
        return f"<AvatarHistory avatar={self.avatar!r} added={self.added!r}>"


class ActivityRecord(Struct):
    """
    Class Representing an Activity Record

    Attributes:
        dId (str): ID of Activity
        name (str): Activity Name
        icon (Avatar): Activity Icon
    """

    dId: str
    name: str
    icon: Avatar

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.avatar, self.dId)


class Record:
    """
    Class Representing A User's Activity History

    Attributes:
        id (int): Internal ID of Record
        date (str): Date This Activity was Played
        duration (int): Duration of Activity Played
        activity_id (str): ID of Activity Played
        discord_id (str): Discord ID of User Playing The Activity
        activity (dict): Dict Of Information Referencing the Activity
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "date",
        "duration",
        "activity_id",
        "discord_id",
        "activity",
    )

    def __init__(self, data: Dict, format: bool) -> None:
        self.id: int = data.get("id")
        self.date: str = (
            humanize_iso_format(data.get("date")) if format else data.get("date")
        )
        self.duration: int = (
            humanize_duration(data.get("duration")) if format else data.get("duration")
        )
        self.activity_id: str = data.get("dActivityId")
        self.discord_id: str = data.get("dUserId")
        self.activity: ActivityRecord = data.get("Activity")

    def __repr__(self) -> str:
        return f"<Record date={self.date!r} duration={self.duration!r}>"
