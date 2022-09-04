from typing import Final, final


@final
class API:
    BASE_URL: Final[str] = "https://api.presencedb.com"
    ICON_BASE: Final[str] = "https://s3.vasc.dev/presencedb/app-icons"
    AVATAR_BASE: Final[str] = "https://s3.vasc.dev/presencedb/avatars"
    HEADERS: Final[str] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50",
        "content-type": "application/json",
    }
