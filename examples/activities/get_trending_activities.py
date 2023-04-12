import asyncio

from presencedb import Client
from presencedb.utils import humanize_duration

client = Client()


async def get_trending_activities():
    activities = await client.get_trending_activities()
    print(f"{activities[0].name} : {humanize_duration(activities[0].duration)}")
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_trending_activities())
