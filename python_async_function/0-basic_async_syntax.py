#!/usr/bin/env python3
"""a module with a function: wait_random
takes an int as an arg (default 10): max delay
waits for the random time then returns the random tome
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for for random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
