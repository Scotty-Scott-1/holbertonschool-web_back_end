#!/usr/bin/env python3
"""import wait random from task 0
new async routine called: wait_n
takes 2 args of type int. n and max_delay
call wait_random n times with max_delay
return a list of delays (floats)
"""


from asyncio import gather
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 args of type int. n and max_delay
    call wait_random n times with max_delay
    return a list of delays (floats)"""

    my_list = [wait_random(max_delay) for _ in range(n)]
    delays = await gather(*my_list)

    return delays
