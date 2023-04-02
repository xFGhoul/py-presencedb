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

from dataclasses import dataclass

from ..constants import API

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
class PlaytimeDate:
    date: str
    seconds: int