#!/usr/bin/python3
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> None:
    start_time = time.time()
    batch = asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    await batch
    end_time = time.time()
    return end_time - start_time