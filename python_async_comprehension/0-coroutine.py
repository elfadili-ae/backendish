#!/usr/bin/python3
import asyncio
import random

async def async_generator():
    res = []
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10
