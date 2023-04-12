import asyncio

from presencedb import Client
from presencedb.enums import ActivityID

client = Client()


async def get_activity(activity_id):
    activity = await client.get_activity(activity_id, format=True)
    print(activity.name)
    print(activity.stats.top_users)
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_activity(ActivityID.SPOTIFY))
