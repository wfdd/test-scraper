
import asyncio
from urllib.request import urlopen

from aiohttp import ClientSession


async def test():
    async with ClientSession() as session, \
               session.get('https://ina.gl/inatsisartut/sammensaetning-af-inatsisartut/'):
        pass

asyncio.get_event_loop().run_until_complete(test())


urlopen('https://ina.gl:443/inatsisartut/sammensaetning-af-inatsisartut/')
