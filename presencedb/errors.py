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

class PresenceDBException(Exception):
    """Base Class For All PresenceDB Errors"""

class UserNotFound(PresenceDBException):
    """Raise an Exception when the User is not found"""


class ActivityNotFound(PresenceDBException):
    """Raise an error when an Activity is not found"""


class HTTPError(PresenceDBException):
    """Raise an error when an unexpected API error occurs"""
