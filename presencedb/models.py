import datetime

from typing import List

class User:
    def __init__(self, user_info: dict) -> None:
        """Object representing JSON response from the presencedb API

        Attributes:
            id: Discord ID of User
            is_system: Determines if user is system (Discord API)
            flags: Discord Flags of a user
            is_bot: Determines if a user is a discord bot (Discord API)
            discriminator: Discord User Discriminator
            createdTimestamp: created timestamp of discord user
            tag: Full Tag (User#0001)
            avatar_url: Discord User Avatar URL
            added: Timestamp of when a user was added to presencedb
            current_activities: list of current activities a user is running
            trending_activities: list of trending activities the user is running
            playtime_dates: list of dates and times that has been recorded

        """
        self.id = int(user_info["id"])
        self.is_system = bool(user_info["system"])
        self.flags = int(user_info["flags"])
        self.is_bot = bool(user_info["bot"])
        self.discriminator = str(user_info["discriminator"])
        self.createdTimestamp = user_info["createdTimestamp"]
        self.tag = str(user_info["tag"])
        self.avatar_url = str(user_info["avatarURL"])
        self.added = user_info["added"]
        self.current_activities = user_info["cache"]["activities"]
        self.top_activities = user_info["topActivities"]
        self.trending_activities = user_info["trendingActivities"]
        self.playtime_dates = user_info["playtimeDates"]

        def __repr__(self):
            return self.tag

class Activity:
    def __init__(self, activity_info: dict) -> None:
        """Object representing JSON response from the presencedb API

        Attributes:
            

        """
        self.name = str(activity_info["name"])
        self.added = activity_info["added"]
        self.playtime_global = int(activity_info["playtimeGlobal"])
        self.playtime_today = int(activity_info["playtimeToday"])
        self.playtime_dates = activity_info["playtimeToday"]
        self.img_url = str(activity_info["imgUrl"])
        self.color = str(activity_info["color"])

        def __repr__(self):
            return self.name
