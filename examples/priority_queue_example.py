import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator_lib.priority_queue import BiDirectionalPriorityQueue

def main():
    queue = BiDirectionalPriorityQueue()

    # Додавання елементів
    queue.enqueue("task1", priority=5)
    queue.enqueue("task2", priority=2)
    queue.enqueue("task3", priority=8)
    queue.enqueue("task4", priority=3)

    print("\nPeek highest:", queue.peek("highest"))
    print("Peek lowest:", queue.peek("lowest"))
    print("Peek oldest:", queue.peek("oldest"))
    print("Peek newest:", queue.peek("newest"))

    print("\nDequeue highest:", queue.dequeue("highest"))
    print("Dequeue lowest:", queue.dequeue("lowest"))
    print("Dequeue oldest:", queue.dequeue("oldest"))
    print("Dequeue newest:", queue.dequeue("newest"))

if __name__ == "__main__":
    main()
