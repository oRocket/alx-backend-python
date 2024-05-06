#!/usr/bin/env python3
"""
Module of asynchronous coroutine that takes in an integer argument
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Generate a random delay between 0 and max_delay seconds (inclusive)
    '''
    delay = random.uniform(0, max_delay)

    '''
    Asynchronously wait for the generated delay
    '''
    await asyncio.sleep(delay)

    '''
    Return the delay after waiting for it
    '''
    return delay
