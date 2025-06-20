import asyncio
from generator_lib.stream_processing import process_large_data_stream

if __name__ == "__main__":
    asyncio.run(process_large_data_stream())