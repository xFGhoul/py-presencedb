import asyncio

from presencedb import Client

client = Client()

async def test_user(id):
    user = await client.get_user(id)
    print(user.top_activities)

loop = asyncio.new_event_loop()
loop.run_until_complete(test_user(433026067050266634))