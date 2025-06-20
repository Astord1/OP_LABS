import heapq
import itertools
from collections import deque

class BiDirectionalPriorityQueue:
    def __init__(self):
        self._heap = []
        self._min_heap = []
        self._counter = itertools.count()
        self._entry_finder = {}  # key: id, value: (priority, count, item)
        self._insertion_order = deque()

    def enqueue(self, item, priority):
        count = next(self._counter)
        entry = (priority, count, item)
        heapq.heappush(self._heap, (-priority, count, item))  # max-heap
        heapq.heappush(self._min_heap, (priority, count, item))  # min-heap
        self._entry_finder[item] = entry
        self._insertion_order.append(item)

    def dequeue(self, mode="highest"):
        if mode == "highest":
            return self._pop_from_heap(self._heap)
        elif mode == "lowest":
            return self._pop_from_heap(self._min_heap)
        elif mode == "oldest":
            if self._insertion_order:
                item = self._insertion_order.popleft()
                self._remove_item(item)
                return item
        elif mode == "newest":
            if self._insertion_order:
                item = self._insertion_order.pop()
                self._remove_item(item)
                return item
        raise IndexError("Queue is empty or invalid mode.")

    def peek(self, mode="highest"):
        if mode == "highest":
            return self._peek_heap(self._heap)
        elif mode == "lowest":
            return self._peek_heap(self._min_heap)
        elif mode == "oldest":
            return self._insertion_order[0] if self._insertion_order else None
        elif mode == "newest":
            return self._insertion_order[-1] if self._insertion_order else None
        return None

    def _pop_from_heap(self, heap):
        while heap:
            _, _, item = heapq.heappop(heap)
            if item in self._entry_finder:
                self._remove_item(item)
                return item
        raise IndexError("Heap is empty.")

    def _peek_heap(self, heap):
        while heap:
            _, _, item = heap[0]
            if item in self._entry_finder:
                return item
            heapq.heappop(heap)  # remove stale
        return None

    def _remove_item(self, item):
        self._entry_finder.pop(item, None)
        try:
            self._insertion_order.remove(item)
        except ValueError:
            pass  # already removed
