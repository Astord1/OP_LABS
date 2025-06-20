import asyncio
from typing import Callable, Any, List, Optional

def async_map_callback(data, callback, done):
    result = []

    def process(index):
        if index >= len(data):
            return done(result)
        callback(data[index], lambda mapped_value: on_mapped(index, mapped_value))

    def on_mapped(index, value):
        result.append(value)
        process(index + 1)

    process(0)

async def async_map_promise(data: List[Any], mapper: Callable[[Any], Any], delay: float = 0) -> List[Any]:
    async def wrapped(item):
        if delay:
            await asyncio.sleep(delay)
        return await mapper(item) if asyncio.iscoroutinefunction(mapper) else mapper(item)

    tasks = [wrapped(item) for item in data]
    return await asyncio.gather(*tasks)

async def async_map_with_abort(data: List[Any], mapper: Callable[[Any], Any], abort_flag: Optional[asyncio.Event] = None):
    result = []

    for item in data:
        if abort_flag and abort_flag.is_set():
            print("Aborted!")
            break
        mapped = await mapper(item) if asyncio.iscoroutinefunction(mapper) else mapper(item)
        result.append(mapped)
    return result
