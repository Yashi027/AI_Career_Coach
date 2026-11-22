"""
Shared Memory
It will act as a common storage for all agents.
"""

class SharedMemory:
    "Share memory accessible by every agent"
    def __init__(self):
        self._memory = {}

    def add(self, key: str, value: str) -> None:
        " Store Data "
        self._memory[key] = value

    def get(self, key: str) -> str:
        " Retrieve Data "
        return self._memory.get(key)

    def exists(self, key: str) -> bool:
        " Check if key exists "
        return key in self._memory

    def clear(self) -> None:
        " Clear Memory "
        self._memory.clear()

    def display(self) -> None:
        " Print Current Memory "
        print("="*25)
        for key, val in self._memory.items():
            print(key)
            print(val)
            print("="*25)
            