import time
import random
from line_profiler import profile


class InMemory:
    """
    A class to simulate an in-memory storage for profiling data.
    This is a placeholder for actual storage logic.
    """

    def __init__(self):
        self.data = {}

    def _simulate_delay(self, slow=False):
        """Simulate a delay to mimic real-world storage operations."""
        if slow:
            time.sleep(random.uniform(1, 5))
        else:
            time.sleep(random.uniform(0.01, 0.5))

    @profile
    def store(self, key, value):
        """Store a value in memory with the given key."""
        if "slow" in key:
            self._simulate_delay(slow=True)
        else:
            self._simulate_delay()
        self.data[key] = value

    @profile
    def retrieve(self, key):
        """Retrieve a value from memory by its key."""
        self._simulate_delay()
        return self.data.get(key)

    def clear(self):
        """Clear all stored data."""
        self.data.clear()
