from typing import Dict, List, Tuple

from .abc import PlaytimeDate, TopUser
from .constants import API
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
    id: class:`int`
        Internal PresenceDB ID of Activity
    name: :class:`str`
        Name of Activity
    dId: :class:`int`
        ID of Activity
    added: :class:`str`
        Date Activity Was Added
    icon: :class:`str`
        Avatar Icon ID
    color: :class:`str`
        Color of Activity
    stats: ActivityStats
        Stats of Activity
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "name",
        "dId",
        "added",
        "icon",
        "color",
        "stats",
    )

    def __init__(self, data: Dict, stats: Dict, should_format: bool) -> None:
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.dId: int = data.get("dId")
        self.added: str = data.get("added")
        self.icon: str = data.get("icon")
        self.color: str = data.get("color")
        self.stats: ActivityStats = ActivityStats(stats, should_format)

        def __repr__(self):
            return self.name

    @property
    def icon_url(self) -> str:
        """Get Icon URL of Activity

        Returns
        -------
        str
            Icon URL
        """
        return f"{API.ICON_BASE}/{self.dId}/{self.icon}"


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
            stats.get("totalDuration")
            if not should_format
            else humanize_duration(stats.get("totalDuration"), HUMANIZE_DAYS)
        )
        self.trending_duration: str = (
            stats.get("trendingDuration")
            if not should_format
            else humanize_duration(stats.get("trendingDuration"), HUMNANIZE_HOURS)
        )
        self.top_users: List[TopUser] = [
            TopUser(**top_user) for top_user in stats.get("topUsers")
        ]
        self.playtime_dates: List[PlaytimeDate] = [
            PlaytimeDate(**playtime_date)
            for playtime_date in stats.get("playtimeDates")
        ]
