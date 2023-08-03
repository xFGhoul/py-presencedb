from typing import Dict, Tuple

from .abc import Avatar


class Session:
    """
    Class Interface Representing User Session

    Attributes
    ----------
    id: :class:`int`
        Current User ID
    """

    __slots__: Tuple[str, ...] = (
        "id",
        "username",
        "global_username",
        "avatar",
        "discriminator",
        "public_flags",
        "flags",
        "banner",
        "banner_color",
        "accent_color",
        "locale",
        "mfa_enabled",
        "premium_type",
        "avatar_decoration",
        "provider",
        "access_token",
        "fetched_at",
    )

    def __init__(self, data: Dict) -> None:
        user: Dict = data.get("user")
        self.id: str = user.get("id")
        self.username: str = user.get("username")
        self.global_username: str = user.get("global_name")
        self.avatar: Avatar = Avatar._from_user(user.get("avatar"), self.id)
        self.discriminator: str = user.get("discriminator")
        self.public_flags: int = user.get("public_flags")
        self.flags: int = user.get("flags")
        self.banner: str = user.get("banner")
        self.banner_color: str = user.get("banner_color")
        self.accent_color: int = user.get("accent_color")
        self.locale: str = user.get("locale")
        self.mfa_enabled: bool = user.get("mfa_enabled")
        self.premium_type: int = user.get("premium_type")
        self.avatar_decoration: str = user.get("avatar_decoration")
        self.provider: str = user.get("provider")
        self.access_token: str = user.get("accessToken")
        self.fetched_at: str = user.get("fetchedAt")
