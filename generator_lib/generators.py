import random
import string

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def random_number_generator():
    while True:
        yield random.randint(1, 100)

def round_robin_generator():
    items = ["A", "B", "C"]
    while True:
        for item in items:
            yield item

def weekday_generator():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        for day in days:
            yield day

def incremental_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

def random_string_generator(length=5):
    while True:
        rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        yield rand_str

def color_cycle_generator():
    colors = ["red", "green", "blue", "yellow", "purple"]
    while True:
        for color in colors:
            yield color

def choose_generator(option):
    generators = [
        fibonacci_generator,
        random_number_generator,
        round_robin_generator,
        weekday_generator,
        incremental_counter,
        random_string_generator,
        color_cycle_generator
    ]
    if 0 <= option < len(generators):
        return generators[option]()
    raise ValueError("Invalid option. Choose 0–6.")
