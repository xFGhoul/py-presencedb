import aiohttp
import pytest

from presencedb.client import Client

USER_ACCOUNT_ID: str = "433026067050266634"


@pytest.mark.asyncio
async def test_fetch_user() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    user = await client.get_user(USER_ACCOUNT_ID)
    await client.cleanup()

    assert user.dId == USER_ACCOUNT_ID
    assert user.name == "ghoul"
