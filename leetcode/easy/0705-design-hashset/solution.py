class MyHashSet:

    def __init__(self):
        # Using chaining to handle collisions; buckets reduce the load factor
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.table[idx]:
            self.table[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.table[idx]