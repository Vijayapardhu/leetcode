# Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

 

 **Example 1:** 

 **Input:**  s = "()"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "()[]{}"

 **Output:**  true

 **Example 3:** 

 **Input:**  s = "(]"

 **Output:**  false

 **Example 4:** 

 **Input:**  s = "([])"

 **Output:**  true

 **Example 5:** 

 **Input:**  s = "([)]"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-09-18T06:29:44.995Z  

```py
class Solution:

    def isValid(self, s: str) -> bool:

        open_b = "([{"       # round, square, curly
        close_b = ")]}"      # round, square, curly
        st = []

        for i in s:

            # Open brackets go into the stack
            if i in open_b:
                st.append(i)

            else:    # When a closed bracket is encountered

                # If stack is empty, sequence is invalid
                if not st:
                    return False

                # Check if stack top is corresponding open bracket
                if ((i == ")" and st[-1] == "(") or
                    (i == "]" and st[-1] == "[") or
                    (i == "}" and st[-1] == "{")):

                    st.pop()

                else:
                    return False

        # Valid only if stack is empty
        return not st
```

---

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)