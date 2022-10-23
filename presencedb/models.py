from dataclasses import dataclass

from ._constants import API
from .utils import humanize_duration, HUMNANIZE_HOURS, HUMANIZE_DAYS

class User:
    def __init__(self, user_info: dict, user_stats: dict, should_format: bool) -> None:
        """
        Object representing JSON response from the presencedb API
        """
        self.id = int(user_info["id"])
        self.dId = int(user_info["dId"])
        self.name = str(user_info["name"])
        self.discriminator = str(user_info["discriminator"])
        self.inactive = bool(user_info["inactive"])
        self.private = bool(user_info["private"])
        self.added = str(user_info["added"])
        self.color = str(user_info["color"])
        self.avatar = str(user_info["avatar"])
        self.plus = bool(user_info["plus"])
        self.timestamp = user_info["tracker"]["timestamp"]
        self.current_activity = [
            CurrentActivity(**activity)
            for activity in user_info["tracker"]["activities"]
        ]
        self.stats = UserStats(user_stats, should_format)
        self.tag = self.name + self.discriminator

        def __repr__(self):
            return self.tag


class UserStats:
    def __init__(self, user_stats: dict, should_format) -> None:
        """
        Object representing JSON response from the presencedb API
        """
        self.total_duration = (
            user_stats["totalDuration"]
            if not should_format
            else humanize_duration(user_stats["totalDuration"], HUMANIZE_DAYS)
        )
        self.trending_duration = (
            user_stats["trendingDuration"]
            if not should_format
            else humanize_duration(user_stats["trendingDuration"], HUMNANIZE_HOURS)
        )
        self.playtime_dates = [
            PlaytimeDate(**playtime_date)
            for playtime_date in user_stats["playtimeDates"]
        ]
        self.top_activites = [
            TopActivity(**activity) for activity in user_stats["topActivities"]
        ]
        self.trending_activities = [
            TrendingActivity(**activity)
            for activity in user_stats["trendingActivities"]
        ]
        self.avatar_history = [
            AvatarHistory(**avatar) for avatar in user_stats["avatarHistory"]
        ]


class ActivityStats:
    """
    Object representing JSON response from the presencedb API
    """

    def __init__(self, activity_stats: dict, should_format: bool) -> None:
        self.total_duration = (
            activity_stats["totalDuration"]
            if not should_format
            else humanize_duration(activity_stats["totalDuration"], HUMANIZE_DAYS)
        )
        self.trending_duration = (
            activity_stats["trendingDuration"]
            if not should_format
            else humanize_duration(activity_stats["trendingDuration"], HUMNANIZE_HOURS)
        )
        self.top_users = [
            TopUser(**top_user) for top_user in activity_stats["topUsers"]
        ]
        self.playtime_dates = [
            PlaytimeDate(**playtime_date)
            for playtime_date in activity_stats["playtimeDates"]
        ]


class Activity:
    def __init__(
        self, activity_info: dict, activity_stats: dict, should_format: bool
    ) -> None:
        """
        Object representing JSON response from the presencedb API
        """
        self.name = str(activity_info["name"])
        self.dId = int(activity_info["dId"])
        self.added = activity_info["added"]
        self.icon = str(activity_info["icon"])
        self.color = str(activity_info["color"])
        self.stats = ActivityStats(activity_stats, should_format)

        def __repr__(self):
            return self.name

        def __post_init__(self):
            self.icon = f"{API.ICON_BASE}/{self.dId}/{self.icon}"


@dataclass
class TopActivity:
    name: str
    dId: int
    icon: str
    duration: int

    def __post_init__(self):
        self.icon = f"{API.ICON_BASE}/{self.dId}/{self.icon}"


@dataclass
class TrendingActivity:
    name: str
    dId: int
    icon: str
    duration: int

    def __post_init__(self):
        self.icon = f"{API.ICON_BASE}/{self.dId}/{self.icon}"


@dataclass
class TopUser:
    name: str
    avatar: str
    discriminator: str
    dId: int
    duration: int

    def __post_init__(self):
        self.avatar = f"{API.AVATAR_BASE}/{self.dId}/{self.avatar}"


@dataclass
class PlaytimeDate:
    date: str
    seconds: int


@dataclass
class CurrentActivity:
    name: str
    id: int


@dataclass
class AvatarHistory:
    id: int
    dUserId: int
    avatar: str
    added: str
    hidden: bool

    def __post_init__(self):
        self.avatar = f"{API.AVATAR_BASE}/{self.dUserId}/{self.avatar}"
