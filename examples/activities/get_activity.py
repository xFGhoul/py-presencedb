import asyncio

from presencedb import Client
from presencedb.enums import Activity

client = Client()


async def get_activity(id):
    activity = await client.get_activity(id, should_format=True)
    print(activity.name)
    print(activity.stats.top_users)


loop = asyncio.new_event_loop()
loop.run_until_complete(get_activity(Activity.SPOTIFY))
