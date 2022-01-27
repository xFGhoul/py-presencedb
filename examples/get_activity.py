import asyncio

from presencedb import Client
from presencedb.enums import ActivityID

client = Client()

async def get_activity(id):
    activity = await client.get_activity(id)
    print(activity.name)

loop = asyncio.new_event_loop()
loop.run_until_complete(get_activity(ActivityID.genshin_impact))
