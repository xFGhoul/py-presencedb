import pytest

from presencedb.client import Client

USER_ACCOUNT_ID: str = "433026067050266634"
OTHER_USER_ACCOUNT_ID: str = "469816379684552706"


@pytest.mark.asyncio
async def test_fetch_user() -> None:
    client = Client()
    async with client:
        user = await client.get_user(USER_ACCOUNT_ID)

        assert user.discord_id == USER_ACCOUNT_ID
        assert user.name == "ghoul"


@pytest.mark.asyncio
async def test_fetch_multiple_users() -> None:
    client = Client()
    async with client:
        users = await client.get_users([USER_ACCOUNT_ID, OTHER_USER_ACCOUNT_ID])

        assert users[0].discord_id == USER_ACCOUNT_ID
        assert users[1].discord_id == OTHER_USER_ACCOUNT_ID
