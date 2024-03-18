#!/usr/bin/env python3
"""async routine called wait_n that takes in 2 int arguments"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    """
    delays = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = await task
            delays.append(delay)
    return delays
