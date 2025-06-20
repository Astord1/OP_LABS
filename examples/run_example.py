from generator_lib.generators import choose_generator
from generator_lib.consumer import consume_with_timeout

def main():
    print("Select a generator:")
    print(" 0 - Fibonacci")
    print(" 1 - Random Number")
    print(" 2 - Round Robin")
    print(" 3 - Weekday")
    print(" 4 - Incremental Counter")
    print(" 5 - Random String")
    print(" 6 - Color Cycle")

    try:
        option = int(input("Enter number (0-6): "))
        gen = choose_generator(option)
        consume_with_timeout(gen, timeout_seconds=5)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
