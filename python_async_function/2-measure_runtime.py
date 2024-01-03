#!/usr/bin/env python3
"""import wait random from task 0
new async routine called: wait_n
takes 2 args of type int. n and max_delay
call wait_random n times with max_delay
return a list of delays (floats)
"""


from asyncio import gather, sleep
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """wait for wait_n tasks. get difference"""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    total = end - start

    return total / n
