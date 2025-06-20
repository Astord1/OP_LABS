from collections import defaultdict
from typing import Callable, Any


class EventEmitter:
    def __init__(self):
        self._listeners = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[[Any], None]) -> Callable[[], None]:
        self._listeners[event].append(callback)

        def unsubscribe():
            self._listeners[event].remove(callback)
        return unsubscribe

    def emit(self, event: str, data: Any = None):
        for callback in self._listeners[event]:
            callback(data)
