import sys
import aiohttp
from typing import Dict, Final, Tuple, final

from yarl import URL

__all__: Tuple[str, ...] = ("API",)


@final
class API:
    """Class Representing Constants For API"""

    BASE: Final[URL] = URL("https://presencedb.com/api")
    ICON: Final[URL] = URL("https://r2.presencedb.com/app-icons")
    AVATAR: Final[URL] = URL("https://r2.presencedb.com/avatars")
    SPOTIFY: Final[URL] = URL("https://www.presencedb.com/spotify.svg")
    VERSION: Final[str] = "2.0.0"
    HEADERS: Final[Dict[str, str]] = {
        "user-agent": f"PresenceDBClient (https://github.com/xFGhoul/py-presencedb {VERSION}) Python/{sys.version_info[0]}.{sys.version_info[1]} aiohttp/{aiohttp.__version__}",
        "content-type": "application/json",
    }
