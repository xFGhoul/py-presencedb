# py-presencedb

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Python API wrapper for the <https://presencedb.com> API

## Installation

**Python 3.11 or higher is required**

Install The PyPi Version:

```sh
py -3 -m pip install -U presencedb
```

You may also install the development version:

```sh
pip install git+https://github.com/xFGhoul/py-presencedb.git
```

## Usage

Quick Example:

```py
import asyncio

from presencedb import Client

client = Client()


async def get_user(id):
    user = await client.get_user(id, format=True)
    print(user.current_activity)
    print(user.stats.top_activities)
    print(user.stats.total_duration)


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user(1234))
```

You can find more examples in the [examples](https://github.com/xFGhoul/py-presencedb/blob/dev/examples/) directory.

## Files and Explanations

`├──`[`.github`](https://github.com/xFGhoul/py-presencedb/blob/dev/.github) — GitHub configuration including CI/CD workflows<br>
`├──`[`docs`](https://github.com/xFGhoul/py-presencedb/blob/dev/docs) — Developer Documentation<br>
`├──`[`tests`](https://github.com/xFGhoul/py-presencedb/blob/dev/tests) — Tests<br>
`├──`[`examples`](https://github.com/xFGhoul/py-presencedb/blob/dev/examples) — Examples Showing How To Use The Wrapper<br>
`├──`[`presencedb`](https://github.com/xFGhoul/py-presencedb/blob/dev/pyprotector) — Source Code Of py-presencedb<br>

> Made With ❤️ By `ghoul#1337`
