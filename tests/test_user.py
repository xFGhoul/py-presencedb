import aiohttp
import pytest

from presencedb.client import Client

USER_ACCOUNT_ID: str = "433026067050266634"
OTHER_USER_ACCOUNT_ID: str = "469816379684552706"


@pytest.mark.asyncio
async def test_fetch_user() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    user = await client.get_user(USER_ACCOUNT_ID)
    await client.cleanup()

    assert user.dId == USER_ACCOUNT_ID
    assert user.name == "ghoul"


@pytest.mark.asyncio
async def test_fetch_multiple_users() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    users = await client.get_users([USER_ACCOUNT_ID, OTHER_USER_ACCOUNT_ID])
    await client.cleanup()

    assert users[0].dId == USER_ACCOUNT_ID
    assert users[1].dId == OTHER_USER_ACCOUNT_ID
