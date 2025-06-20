import time
from generator_lib.memoization import memoize

@memoize(max_size=3, policy="lru")
def slow_add(x, y):
    print(f"Computing slow_add({x}, {y})")
    time.sleep(1)
    return x + y

@memoize(max_size=2, policy="lfu")
def multiply(x, y):
    print(f"Computing multiply({x}, {y})")
    return x * y

@memoize(policy="time", expiry_seconds=2)
def square(x):
    print(f"Computing square({x})")
    return x * x

def custom_eviction_policy(cache):
    # Видаляє ключ, де аргументи x == 42, якщо знайдено, інакше перший
    for key in cache:
        if key[0] == 42:
            return key
    return next(iter(cache))

@memoize(max_size=2, policy="custom", custom_eviction=custom_eviction_policy)
def greet(name):
    print(f"Computing greet({name})")
    return f"Hello, {name}!"

def main():
    print("\n--- LRU ---")
    print(slow_add(1, 2))
    print(slow_add(1, 2))
    print(slow_add(2, 3))
    print(slow_add(3, 4))
    print(slow_add(1, 2))

    print("\n--- LFU ---")
    print(multiply(2, 3))
    print(multiply(2, 3))
    print(multiply(4, 5))
    print(multiply(6, 7))
    print(multiply(2, 3))

    print("\n--- Time-based expiry ---")
    print(square(10))
    time.sleep(3)
    print(square(10))

    print("\n--- Custom policy ---")
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))
    print(greet("Alice"))

if __name__ == "__main__":
    main()
