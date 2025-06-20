import time

def consume_with_timeout(iterator, timeout_seconds=5, delay=0.5):
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        try:
            value = next(iterator)
            print(value)
            time.sleep(delay)
        except StopIteration:
            print("Iterator is exhausted.")
            break
