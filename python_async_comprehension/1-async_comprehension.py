#!/usr/bin/python3
import asyncio
from typing import List

async_generator = __import__('0-coroutine').async_generator

async def async_comprehension() -> List[float]:
    res = []
    async for val in async_generator():
        res.append(val)
    return res