import asyncio

from presencedb import Client

client = Client()


async def get_user(discord_id):
    user = await client.get_user(discord_id, should_format=True)
    print(user.current_activities)
    print(user.stats.top_activities)
    print(user.stats.total_duration)
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user(1234))
