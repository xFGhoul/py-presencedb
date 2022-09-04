import asyncio

from presencedb import Client
from presencedb.utils import humanize_duration

client = Client()


async def get_top_activities(id):
    activities = await client.get_top_activities()
    print(
        activities
    )  # [TopActtivity(name=..., dId=..., duration=..., icon=...), TopActivity(name=..., dId=..., duration=..., icon=...)]
    # OR
    print(
        f"{activities[0].name} : {humanize_duration(activities[0].duration)}"
    )  # Spotify: x days


loop = asyncio.new_event_loop()
loop.run_until_complete(get_top_activities())
