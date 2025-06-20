# Generator Lib

Python-бібліотека генераторів

## Приклади використання

```python
from generator_lib.generators import fibonacci_generator
from generator_lib.consumer import consume_with_timeout

consume_with_timeout(fibonacci_generator(), timeout_seconds=5)