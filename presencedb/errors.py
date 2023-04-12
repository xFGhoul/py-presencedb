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
    detail: :class:`str`
        The details of this request
    status_code: :class:`int`
        The HTTP status code for this request.
    """

    def __init__(self, detail: str, status_code: int) -> None:
        self.detail: str = detail
        self.status_code: int = status_code
        super().__init__(detail, status_code)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} detail={self.detail} status_code={self.status_code}>"


class UserNotFound(PresenceDBException):
    """Raised When User Could Not Be Found

    Attributes
    -----------
    detail: :class:`str`
        The details of this request
    status_code: :class:`int`
        The HTTP status code for this request.
    """

    def __init__(self, detail: str, status_code: int) -> None:
        super().__init__(detail="User Could Not Be Found", status_code=404)


class ActivityNotFound(PresenceDBException):
    """Raised When User Could Not Be Found

    Attributes
    -----------
    detail: :class:`str`
        The details of this request
    status_code: :class:`int`
        The HTTP status code for this request.
    """

    def __init__(self, detail: str, status_code: int) -> None:
        super().__init__(detail="Activity Could Not Be Found", status_code=404)


class ActivitiesNotFound(PresenceDBException):
    """Raised When User Could Not Be Found

    Attributes
    -----------
    detail: :class:`str`
        The details of this request
    status_code: :class:`int`
        The HTTP status code for this request.
    """

    def __init__(self, detail: str, status_code: int) -> None:
        super().__init__(detail="Activities Could Not Be Found", status_code=404)


class HTTPError(PresenceDBException):
    """Raised When User Could Not Be Found

    Attributes
    -----------
    detail: :class:`str`
        The details of this request
    status_code: :class:`int`
        The HTTP status code for this request.
    """

    def __init__(self, detail: str, status_code: int) -> None:
        super().__init__(
            detail="Activities Could Not Be Found", status_code=status_code
        )
