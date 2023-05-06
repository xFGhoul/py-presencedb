from dataclasses import dataclass
from typing import Dict, List, Tuple

from .abc import PlaytimeDate, TopActivity, TrendingActivity, Avatar
from .utils import HUMANIZE_DAYS, HUMNANIZE_HOURS, humanize_duration

__all__: Tuple[str, ...] = (
    "User",
    "UserStats",
)


class User:
    """
    Class Interface Containing User Attributes

    Attributes
    ----------
    id: :class:`int`
        PresenceDB Internal User ID
    dId: :class:`int`
        User Discord ID
    name: :class:`str`
        User's Name
    discriminator: :class:`str`
        User's Discord Discriminator
    inactive: :class:`str`
        Returns a Date of when The User Became Inactive
    added: :class:`str`
        Date User's Account Was Added
    color: :class:`str`
        Color Of User's Account
    avatar: :class:`Avatar`
        User Avatar
    plus: :class:`bool`
        If The User Has Subscribed To PresenceDB Plus
    tracker: :class:`Dict`
        Information about Current User Activity
    timestamp: :class:`str`
        Timestamp of Current Activity
    current_activities: List[CurrentActivity]
        List of Current User Activities
    stats: UserStats
        Object Representing User Statistics
    tag: :class:`str`
        Combination of `self.name` + `self.discriminator`
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "dId",
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

    def __init__(self, data: Dict, stats: Dict, should_format: bool) -> None:
        self.id: int = data.get("id")
        self.dId: int = data.get("dId")
        self.name: str = data.get("name")
        self.discriminator: str = data.get("discriminator")
        self.inactive: str = data.get("inactiveSince")
        self.private: bool = data.get("private")
        self.added: str = data.get("added")
        self.color: str = data.get("color")
        self.avatar: Avatar = Avatar._from_user(data.get("avatar"), self.dId)
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
        self.stats: UserStats = UserStats(stats, should_format)
        self.tag: str = self.name + f"#{self.discriminator}"

        def __repr__(self):
            return f"<User tag={self.tag}>"

        def __eq__(self, other):
            return self.id == other.id

        def __hash__(self) -> int:
            return hash(self.id)


class UserStats:
    """
    Class Interface Representing Stats of a User

    Attributes
    ----------
    total_duration: :class:`str`
        Total duration of activity recorded
    trending_duration: :class:`str`
        Trending Duration of Activities
    top_users: List[TopUser]
        List of Top Users For The Activity
    playtime_dates: List[PlaytimeDate]
        List of Playtime Dates For Activity
    top_activities: List[TopActivity]
        List of Top Activities For User
    trending_activities: List[TrendingActivity]
        List of Trending Activities For User
    avatar_history: List[AvatarHistory]
        List of Avatars Users Recorded
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

    def __init__(self, stats: Dict, should_format) -> None:
        self.total_duration: str = (
            stats.get("totalDuration")
            if not should_format
            else humanize_duration(stats.get("totalDuration"), HUMANIZE_DAYS)
        )
        self.trending_duration: str = (
            stats.get("trendingDuration")
            if not should_format
            else humanize_duration(stats.get("trendingDuration"), HUMNANIZE_HOURS)
        )
        self.playtime_dates: List[PlaytimeDate] = [
            PlaytimeDate(**playtime_date)
            for playtime_date in stats.get("playtimeDates")
        ]
        self.top_activities: List[TopActivity] = [
            TopActivity(**activity) for activity in stats.get("topActivities")
        ]
        self.trending_activities: List[TrendingActivity] = [
            TrendingActivity(**activity) for activity in stats.get("trendingActivities")
        ]
        self.avatar_history: List[AvatarHistory] = [
            AvatarHistory(**avatar) for avatar in stats.get("avatarHistory")
        ]
        self.records: List[Record] = [
            Record(**record) for record in stats.get("records")
        ]


@dataclass
class CurrentActivity:
    """
    Class Representing A Current Activity

    Attributes
    ----------
    name: :class:`str`
        Name of Activity
    id: :class:`int`
        ID of Activity
    """

    name: str
    id: int


@dataclass
class AvatarHistory:
    """
    Class Representing A User's Avatar History

    Attributes
    ----------
    id: :class:`int`
        ID of Avatar
    dId: :class:`int`
        Discord ID Pertaining to Avatar
    avatar: :class:`Avatar`
        Avatar
    added: :class:`str`
        Date Avatar Was Added
    hidden: :class:`bool`
        Whether Avatar Is Hidden From Site
    """

    id: int
    dUserId: int
    avatar: Avatar
    added: str
    hidden: bool

    def __post_init__(self):
        self.avatar = Avatar._from_user(self.avatar, self.dUserId)


@dataclass
class ActivityRecord:
    """Class Representing an Activity Record

    Attributes
    ----------
    dId: :class:`str`
        ID of Activity
    name: :class:`str`
        Activity Name
    icon: :class:`Avatar`
        Activity Icon
    """

    dId: str
    name: str
    icon: Avatar

    def __post_init__(self):
        self.icon = Avatar._from_activity(self.avatar, self.dId)


@dataclass
class Record:
    """
    Class Representing A User's Activity History

    Attributes
    ----------
    id: :class:`int`
        Internal ID of Record
    date: :class:`str`
        Date This Activity was Played
    duration: :class:`int`
        Duration of Activity Played
    dActivityId: :class:`str`
        ID of Activity Played
    dUserId: :class:`str`
        Discord ID of User Playing The Activity
    Activity: :class:`dict`
        Dict Of Information Referencing the Activity
    """

    id: int
    date: str
    duration: int
    dActivityId: str
    dUserId: str
    Activity: ActivityRecord
