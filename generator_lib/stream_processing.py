import asyncio
import random

async def large_data_async_generator(limit=1000):
    """Імітація великого потоку даних, який генерує числа поступово."""
    for i in range(limit):
        # Імітація затримки на отримання даних (наприклад, з мережі/файлу)
        await asyncio.sleep(0.001)
        yield random.randint(1, 1000)

async def process_large_data_stream():
    """Приклад обробки великого потоку асинхронно."""
    total = 0
    count = 0
    async for value in large_data_async_generator():
        total += value
        count += 1
        if count % 100 == 0:
            print(f"Оброблено {count} елементів, поточна сума: {total}")
    print(f"Загальна сума: {total}")
