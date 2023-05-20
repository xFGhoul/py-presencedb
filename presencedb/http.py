import aiohttp
import asyncio
import logging

from yarl import URL
from typing import Any, Optional

from .errors import HTTPException, PresenceDBError, NotFound
from .constants import API

logger = logging.getLogger(__name__)


class Route:
    def __init__(self, method: str, path: str, **parameters: Any):
        if parameters:
            try:
                path = path.format(**parameters)
            except IndexError:
                pass

        self.path: str = path
        self.url: URL = URL(API.BASE / self.path)
        self.method: str = method


class HTTP:
    def __init__(
        self,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        self.session: Optional[aiohttp.ClientSession] = session
        self.lock: asyncio.Lock = asyncio.Lock()

    async def create_client_session(self) -> None:
        self.session = aiohttp.ClientSession(headers=API.HEADERS)

    # credit from nextchai
    async def request(self, route: Route, **kwargs) -> None:
        if self.session is None:
            await self.create_client_session()

        response: Optional[aiohttp.ClientResponse] = None
        async with self.lock:
            for tries in range(5):
                async with self.session.request(
                    route.method, route.url, **kwargs
                ) as response:
                    data = await response.json()
                    if 300 > response.status >= 200:
                        return data

                    if response.status == 429:
                        headers = response.headers
                        retry_after: float = float(headers["x-ratelimit-reset"])
                        if retry_after == 0 and not headers.get(
                            "x-ratelimit-remaining"
                        ):
                            retry_after: float = float(headers["Retry-After"])

                        logger.warning(
                            f"We Are Gettng Ratelimited! Try Again In {retry_after} seconds"
                        )
                        await asyncio.sleep(retry_after)
                        continue

                    if response.status in {
                        500,
                        502,
                        504,
                    }:
                        await asyncio.sleep(1 + tries * 2)
                        continue

                    if response.status == 400:
                        raise NotFound(response, data)
                    else:
                        raise HTTPException(response, data)

        if response is not None:
            if response.status >= 500:
                raise PresenceDBError(response, data)

            raise HTTPException(response, data)

        raise RuntimeError("Unreachable code in HTTP handling")
