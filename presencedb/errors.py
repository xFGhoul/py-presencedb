from typing import Tuple, Optional, Union, Any, Dict
from aiohttp import ClientResponse

__all__: Tuple[str, ...] = (
    "PresenceDBException",
    "HTTPException",
    "NotFound",
    "PresenceDBError",
)


class PresenceDBException(Exception):
    """The base Tixte Exception. All Tixte Exceptions inherit from this."""

    __slots__: Tuple[str, ...] = ()


class HTTPException(PresenceDBException):
    """An exception raised when an HTTP Exception occurs from the API.

    Attributes
    ----------
    response: :class:`aiohttp.ClientResponse`
        The response from the API.
    data: :class:`Any`
        The data returned from the API.
    """

    __slots__: Tuple[str, ...] = (
        "response",
        "data",
    )

    def __init__(
        self,
        response: Optional[ClientResponse] = None,
        data: Optional[Union[Dict[Any, Any], Any]] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.response: Optional[ClientResponse] = response
        self.data: Any = data

        self.message: Optional[str]
        self.success: Optional[str]

        if isinstance(data, dict):
            self.message = data.get("error", {})
            self.success = data.get("success", {})
        else:
            self.message = None
            self.success = None

        super().__init__(
            f'{self.success or "No code."}: {self.message or "No message"}.',
            *args,
            **kwargs,
        )


class NotFound(HTTPException):
    """Raised When Object Could Not Be Found

    This inherits from :class:`HTTPException`.
    """

    __slots__: Tuple[str, ...] = ()


class PresenceDBError(HTTPException):
    """Raised When Internal Server Error Occurs

    This inherits from :class:`HTTPException`.
    """

    __slots__: Tuple[str, ...] = ()
