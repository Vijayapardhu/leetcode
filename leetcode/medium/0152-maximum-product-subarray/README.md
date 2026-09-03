# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return  *the product*.

The test cases are generated so that the answer will fit in a  **32-bit**  integer.

 **Note**  that the product of an array with a single element is the value of that element.

 

 **Example 1:** 

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

 **Example 2:** 

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 95.58%)  
**Memory:** 19.8 MB (beats 44.78%)  
**Submitted:** 2026-09-03T15:54:59.047Z  

```py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize tracking variables with the first element
        max_so_far = min_so_far = res = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # If current number is negative, swapping max and min 
            # handles the flip in sign for product calculations
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            
            res = max(res, max_so_far)
            
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)