from generator_lib.logging_decorator import log

@log(level="INFO")
def add(x, y):
    return x + y

@log(level="ERROR")
def fail():
    raise ValueError("Something went wrong")

if __name__ == "__main__":
    print(add(3, 4))
    try:
        fail()
    except:
        pass
