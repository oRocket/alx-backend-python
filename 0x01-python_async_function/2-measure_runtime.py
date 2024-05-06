#!/usr/bin/env python3
"""
Module that Create a measure_time function with integers n and max_delay as arguments
"""
import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay), and return total_time / n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


'''Test the function
'''
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
