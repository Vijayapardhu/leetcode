# Remove All Adjacent Duplicates In String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` consisting of lowercase English letters. A  **duplicate removal**  consists of choosing two  **adjacent**  and  **equal**  letters and removing them.

We repeatedly make  **duplicate removals**  on `s` until we no longer can.

Return  *the final string after all such duplicate removals have been made*. It can be proven that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

 **Example 2:** 

```
Input: s = "azxxzy"
Output: "ay"

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 16 ms (beats 86.42%)  
**Memory:** 20 MB (beats 66.28%)  
**Submitted:** 2026-09-18T05:02:46.218Z  

```py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for char in s:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
```

---

[View on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)