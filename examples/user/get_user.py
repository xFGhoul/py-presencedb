import asyncio

from presencedb import Client
import presencedb

client = Client()
discord_id = 1234


async def get_user(id):
    user = await client.get_user(discord_id, should_format=True)
    print(user.current_activity)
    print(user.stats.top_activites)
    print(user.stats.total_duration)


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user())
