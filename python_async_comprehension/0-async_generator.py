#!/usr/bin/env python3
"""an async generato that yeilds a random numberr"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """in a loop of 10, wait one second, yeild a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
