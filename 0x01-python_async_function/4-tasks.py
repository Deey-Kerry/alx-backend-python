#!/usr/bin/env python3
"""code from wait_n and alter it into a new function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """the code from wait_n and alter it into a new function
    task_wait_n
    """
    delays = []
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = await task
            delays.append(delay)
    return delays
