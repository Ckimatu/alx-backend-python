#!/usr/bin/env python3

"""
file for function measure_time
"""
import time
from typing import List
from asyncio import run, create_task, gather
from random import uniform

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per task.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: Average time per task.
    """
    # Start measuring the execution time
    start_time = time.time()

    # Run wait_n coroutine with specified no. of tasks and maximum delay
    run(wait_n(n, max_delay))

    # Calculate the total elapsed time
    total_time = time.time() - start_time

    # Calculate the average time per task
    average_time = total_time / n

    return average_time
