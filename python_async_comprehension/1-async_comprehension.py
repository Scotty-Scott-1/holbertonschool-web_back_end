#!/usr/bin/env python3
"""collect 10 random numbers
using an async comprehensingover async_generator,
then return the 10 random numbers."""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers
    using an async comprehensingover async_generator,
    then return the 10 random numbers."""
    result = [i async for i in async_generator()]
    return result
