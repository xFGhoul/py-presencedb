import pytest

from presencedb.client import Client
from presencedb.enums import ActivityID


@pytest.mark.asyncio
async def test_fetch_activity() -> None:
    client = Client()
    async with client:
        activity = await client.get_activity(ActivityID.VSCODE)

        assert activity.name == "Visual Studio Code"


@pytest.mark.asyncio
async def test_fetch_multiple_activities() -> None:
    client = Client()
    async with client:
        activities = await client.get_activities(
            [ActivityID.VSCODE, ActivityID.VALORANT]
        )

        assert activities[0].name == "Visual Studio Code"
        assert activities[1].name == "VALORANT"


@pytest.mark.asyncio
async def test_fetch_top_activities() -> None:
    client = Client()
    async with client:
        top_activities = await client.get_top_activities()

        assert top_activities[0].name == "Spotify"


@pytest.mark.asyncio
async def test_fetch_trending_activities() -> None:
    client = Client()
    async with client:
        trending_activities = await client.get_trending_activities()

        assert trending_activities[0].name == "Spotify"
