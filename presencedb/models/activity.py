"""
                                                            _ _     
                                                           | | |    
  _ __  _   _   _ __  _ __ ___  ___  ___ _ __   ___ ___  __| | |__  
 | '_ \| | | | | '_ \| '__/ _ \/ __|/ _ \ '_ \ / __/ _ \/ _` | '_ \ 
 | |_) | |_| | | |_) | | |  __/\__ \  __/ | | | (_|  __/ (_| | |_) |
 | .__/ \__, | | .__/|_|  \___||___/\___|_| |_|\___\___|\__,_|_.__/ 
 | |     __/ | | |                                                  
 |_|    |___/  |_|                                                  

 Made With ❤️ By Ghoul
"""

from typing import Dict
from dataclasses import dataclass

from .abc import TopUser, PlaytimeDate
from ..constants import API
from ..utils import humanize_duration, HUMNANIZE_HOURS, HUMANIZE_DAYS

class Activity:
    def __init__(
        self, activity_info: Dict, activity_stats: Dict, should_format: bool
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