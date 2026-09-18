# Design HashSet

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

 

 **Example 1:** 

```
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

 

 **Constraints:** 

- 0 <= key <= 106
- At most 104 calls will be made to add, remove, and contains.

## Solution

**Language:** Python  
**Runtime:** 16 ms (beats 95.98%)  
**Memory:** 24.2 MB (beats 89.20%)  
**Submitted:** 2026-09-18T14:42:45.817Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/design-hashset/)