#!/usr/bin/env python3

"""
file that contains the task_wait_random function
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that waits for a random delay
    between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay for the task.

    Returns:
        asyncio.Task: Task object that represents the waiting process.
    """
    # Create an awaitable coroutine using  wait_random function
    coro = wait_random(max_delay)

    # Create a Task from the coroutine
    task = asyncio.create_task(coro)

    return task
