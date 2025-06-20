import time
import functools
from collections import OrderedDict, defaultdict

class Memoizer:
    def __init__(self, func, max_size=None, policy="lru", expiry_seconds=None, custom_eviction=None):
        self.func = func
        self.max_size = max_size
        self.policy = policy
        self.expiry_seconds = expiry_seconds
        self.custom_eviction = custom_eviction

        self.cache = {}
        self.usage_order = OrderedDict()  # for LRU
        self.usage_freq = defaultdict(int)  # for LFU
        self.timestamps = {}  # for time-based expiry

    def _evict(self):
        if self.policy == "lru":
            evict_key = next(iter(self.usage_order))
        elif self.policy == "lfu":
            evict_key = min(self.usage_freq, key=self.usage_freq.get)
        elif self.policy == "time":
            now = time.time()
            expired_keys = [k for k, t in self.timestamps.items() if now - t > self.expiry_seconds]
            if expired_keys:
                evict_key = expired_keys[0]
            else:
                return  # нічого не видалено
        elif self.policy == "custom" and self.custom_eviction:
            evict_key = self.custom_eviction(self.cache)
        else:
            return
        self.cache.pop(evict_key, None)
        self.usage_order.pop(evict_key, None)
        self.usage_freq.pop(evict_key, None)
        self.timestamps.pop(evict_key, None)

    def __call__(self, *args):
        key = args
        now = time.time()

        if key in self.cache:
            # оновити метадані
            if self.policy == "lru":
                self.usage_order.move_to_end(key)
            if self.policy == "lfu":
                self.usage_freq[key] += 1
            if self.policy == "time":
                self.timestamps[key] = now
            return self.cache[key]

        # новий розрахунок
        result = self.func(*args)

        # перевірити та очистити кеш при потребі
        if self.max_size is not None and len(self.cache) >= self.max_size:
            self._evict()

        # записати у кеш
        self.cache[key] = result
        if self.policy == "lru":
            self.usage_order[key] = None
        if self.policy == "lfu":
            self.usage_freq[key] = 1
        if self.policy == "time":
            self.timestamps[key] = now

        return result


def memoize(func=None, *, max_size=None, policy="lru", expiry_seconds=None, custom_eviction=None):
    if func is None:
        return lambda f: Memoizer(f, max_size=max_size, policy=policy, expiry_seconds=expiry_seconds, custom_eviction=custom_eviction)
    return Memoizer(func, max_size=max_size, policy=policy, expiry_seconds=expiry_seconds, custom_eviction=custom_eviction)
