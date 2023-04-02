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

from .presencedb import Client
from .utils import icon_id_to_bytes, humanize_duration, HUMANIZE_DAYS, HUMNANIZE_HOURS
from .errors import *
from .enums import Activity

__version__ = "0.0.2"
__author__ = "Ghoul"
__license__ = "MIT"