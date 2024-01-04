#!/usr/bin/env python3
"""
execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.

"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.

    """
    start: float = time.time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end: float = time.time()

    result: float = end - start
    return result
