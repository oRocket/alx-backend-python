#!/usr/bin/env python3
"""
Module that write an async routine called wait_n that takes in 2 int arguments
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn `wait_random` coroutine `n` times
    with the specified `max_delay`.
    Return a list of all the delays in ascending order.
    """
    """Create a list to store the delays"""
    delays = []

    """Asynchronously spawn `wait_random` coroutine `n` times"""
    for _ in range(n):
        """Append the result (delay) of each coroutine to the delays list"""
        delays.append(await wait_random(max_delay))

    """Return the list of delays sorted in ascending order"""
    return sorted(delays)
