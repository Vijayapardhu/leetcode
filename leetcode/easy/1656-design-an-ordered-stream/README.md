# Design an Ordered Stream

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

There is a stream of `n` `(idKey, value)` pairs arriving in an  **arbitrary**  order, where `idKey` is an integer between `1` and `n` and `value` is a string. No two pairs have the same `id`.

Design a stream that returns the values in  **increasing order of their IDs**  by returning a  **chunk**  (list) of values after each insertion. The concatenation of all the  **chunks**  should result in a list of the sorted values.

Implement the `OrderedStream` class:

- OrderedStream(int n) Constructs the stream to take n values.
- String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

 

 **Example:** 

```
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.

```

 

 **Constraints:** 

- 1 <= n <= 1000
- 1 <= id <= n
- value.length == 5
- value consists only of lowercase letters.
- Each call to insert will have a unique id.
- Exactly n calls will be made to insert.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 17.13%)  
**Memory:** 20 MB (beats 72.27%)  
**Submitted:** 2026-09-18T14:43:29.955Z  

```py
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        res = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/design-an-ordered-stream/)