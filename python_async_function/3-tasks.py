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

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """calls coroutine of wait random"""
    async def awaiting():
        """returns a random delay"""
        return await wait_random(max_delay)

    task = asyncio.create_task(awaiting())
    return task
