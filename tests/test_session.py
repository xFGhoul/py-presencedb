import pytest

from presencedb.client import Client


@pytest.mark.asyncio
async def test_user_session() -> None:
    client = Client()
    async with client:
        session = await client.get_session()

        assert session.global_username == "ghoul"
