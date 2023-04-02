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

from .abc import TopActivity, TrendingActivity
from ..constants import API
from ..utils import humanize_duration, HUMNANIZE_HOURS, HUMANIZE_DAYS

class User:
    def __init__(self, user_info: Dict, user_stats: Dict, should_format: bool) -> None:
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
        self.timestamp = user_info["tracker"]["timestamp"] if user_info["tracker"] else None
        self.current_activity = [
            CurrentActivity(**activity)
            for activity in user_info["tracker"]["activities"]
        ]
        self.stats = UserStats(user_stats, should_format)
        self.tag = self.name + self.discriminator

        def __repr__(self):
            return self.tag
        
class UserStats:
    def __init__(self, user_stats: Dict, should_format) -> None:
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
        
@dataclass
class CurrentActivity:
    name: str
    id: int
    
@dataclass
class PlaytimeDate:
    date: str
    seconds: int
        
@dataclass
class AvatarHistory:
    id: int
    dUserId: int
    avatar: str
    added: str
    hidden: bool

    def __post_init__(self):
        self.avatar = f"{API.AVATAR_BASE}/{self.dUserId}/{self.avatar}"