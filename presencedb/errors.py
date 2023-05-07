from typing import Tuple

__all__: Tuple[str, ...] = (
    "PresenceDBException",
    "UserNotFound",
    "ActivityNotFound",
    "HTTPError",
    "ActivitiesNotFound",
)


class PresenceDBException(Exception):
    """Generic API Exception For PresenceDB

    Attributes
    -----------
    message: :class:`str`
        The messages of this request
    """

    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(message)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} message={self.message}>"


class UserNotFound(PresenceDBException):
    """Raised When User Could Not Be Found"""

    def __init__(self, message: str) -> None:
        super().__init__(message="User Could Not Be Found")


class ActivityNotFound(PresenceDBException):
    """Raised When User Could Not Be Found"""

    def __init__(self, message: str) -> None:
        super().__init__(message="Activity Could Not Be Found")


class ActivitiesNotFound(PresenceDBException):
    """Raised When User Could Not Be Found"""

    def __init__(self, message: str) -> None:
        super().__init__(message="Activities Could Not Be Found")


class HTTPError(PresenceDBException):
    """Raised When User Could Not Be Found"""

    def __init__(self, message: str) -> None:
        super().__init__(message="Activities Could Not Be Found")
