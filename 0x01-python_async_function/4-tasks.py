#!/usr/bin/env python3

"""
file for function task_wait_n
"""
import asyncio
from typing import List
from random import uniform


async def task_wait_random(max_delay: int) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)

    return await asyncio.gather(*tasks)
