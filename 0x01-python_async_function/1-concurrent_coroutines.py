#!/usr/bin/env python3

"""
file for the wait_n coroutine
"""
import asyncio
from typing import List
from random import randint
from asyncio.tasks import wait

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        await task
        delays.append(task.result())

    return delays
