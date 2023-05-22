from typing import Dict, List, Tuple

from .abc import PlaytimeDate, TopUser, Avatar
from .utils import HUMANIZE_DAYS, HUMNANIZE_HOURS, humanize_duration

__all__: Tuple[str, ...] = (
    "Activity",
    "ActivityStats",
)


class Activity:
    """
    Class Interface Representing An Activity

    Attributes
    ----------
    id: :class:`int`
        Internal PresenceDB ID of Activity
    name: :class:`str`
        Name of Activity
    discord_id: :class:`int`
        ID of Activity
    added: :class:`str`
        Date Activity Was Added
    icon: :class:`Avatar`
        Activity Icon
    color: :class:`str`
        Color of Activity
    stats: ActivityStats
        Stats of Activity
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "name",
        "discord_id",
        "added",
        "icon",
        "color",
        "stats",
    )

    def __init__(self, data: Dict, stats: Dict, should_format: bool) -> None:
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.discord_id: int = data.get("dId")
        self.added: str = data.get("added")
        self.icon: Avatar = Avatar._from_activity(data.get("icon"), self.discord_id)
        self.color: str = data.get("color")
        self.stats: ActivityStats = ActivityStats(stats, should_format)

    def __repr__(self) -> str:
        return f"<Activity name={self.name!r}>"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


class ActivityStats:
    """
    Class Representing Stats of an Activity

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
    """

    def __init__(self, stats: Dict, should_format: bool) -> None:
        self.total_duration: str = (
            humanize_duration(stats.get("totalDuration"), HUMANIZE_DAYS)
            if should_format
            else stats.get("totalDuration")
        )
        self.trending_duration: str = (
            humanize_duration(stats.get("trendingDuration"), HUMNANIZE_HOURS)
            if should_format
            else stats.get("trendingDuration")
        )
        self.top_users: List[TopUser] = [
            TopUser(**top_user) for top_user in stats.get("topUsers")
        ]
        self.playtime_dates: List[PlaytimeDate] = [
            PlaytimeDate(**playtime_date)
            for playtime_date in stats.get("playtimeDates")
        ]

    def __repr__(self) -> str:
        return f"<ActivityStats total_duration={self.total_duration!r}>"
