import aiohttp
import pytest

from presencedb.client import Client
from presencedb.enums import ActivityID


@pytest.mark.asyncio
async def test_fetch_activity() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    activity = await client.get_activity(ActivityID.VSCODE)
    await client.cleanup()

    assert activity.color == "#FFFFFF"
    assert activity.name == "Visual Studio Code"


@pytest.mark.asyncio
async def test_fetch_multiple_activities() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    activities = await client.get_activities([ActivityID.VSCODE, ActivityID.VALORANT])
    await client.cleanup()

    assert activities[0].name == "Visual Studio Code"
    assert activities[1].name == "VALORANT"


@pytest.mark.asyncio
async def test_fetch_top_activities() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    top_activities = await client.get_top_activities()
    await client.cleanup()

    assert top_activities[0].name == "Spotify"


@pytest.mark.asyncio
async def test_fetch_trending_activities() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    trending_activities = await client.get_trending_activities()
    await client.cleanup()

    assert trending_activities[0].name == "Spotify"
