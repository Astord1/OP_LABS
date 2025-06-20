import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from generator_lib.async_array_utils import async_map_callback, async_map_promise, async_map_with_abort

def multiply_by_two_cb(x, callback):
    callback(x * 2)

async def multiply_by_two_async(x):
    await asyncio.sleep(0.1)
    return x * 2

def example_callback():
    def done(result):
        print("Callback result:", result)

    print("Running callback-based async map...")
    async_map_callback([1, 2, 3], multiply_by_two_cb, done)

async def example_promise():
    print("Running promise-style async map...")
    result = await async_map_promise([1, 2, 3], multiply_by_two_async)
    print("Promise result:", result)

async def example_abort():
    print("Running abortable async map...")
    abort_event = asyncio.Event()

    async def delayed_mapper(x):
        if x == 2:
            abort_event.set()
        await asyncio.sleep(0.2)
        return x * 3

    result = await async_map_with_abort([1, 2, 3, 4], delayed_mapper, abort_flag=abort_event)
    print("Abortable result:", result)

if __name__ == "__main__":
    example_callback()
    asyncio.run(example_promise())
    asyncio.run(example_abort())
