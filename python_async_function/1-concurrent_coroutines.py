#!/usr/bin/env python3
"""import wait random from task 0
new async routine called: wait_n
takes 2 args of type int. n and max_delay
call wait_random n times with max_delay
return a list of delays (floats)
"""


from asyncio import gather, sleep
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 args of type int. n and max_delay
    call wait_random n times with max_delay
    return a list of delays (floats)"""

    async def delay() -> None:
        """wait for the required time and append to list"""
        delay = await wait_random(max_delay)
        await sleep(delay)
        result_list.append(delay)

    result_list: List[float] = []

    my_list = [delay() for _ in range(n)]

    await gather(*my_list)

    return result_list
