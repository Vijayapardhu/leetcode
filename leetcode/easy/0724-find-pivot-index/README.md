# Find Pivot Index

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `nums`, calculate the  **pivot index**  of this array.

The  **pivot index**  is the index where the sum of all the numbers  **strictly**  to the left of the index is equal to the sum of all the numbers  **strictly**  to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return  *the  **leftmost pivot index***. If no such index exists, return `-1`.

 

 **Example 1:** 

```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

```

 **Example 2:** 

```
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

 **Example 3:** 

```
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -1000 <= nums[i] <= 1000

 

 **Note:**  This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 89.29%)  
**Memory:** 20.3 MB (beats 46.85%)  
**Submitted:** 2026-09-03T15:56:02.640Z  

```py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            # The right sum is total - left_sum - current element
            if left_sum == (total_sum - left_sum - val):
                return i
            left_sum += val
            
        return -1 # Return -1 if no pivot index is found
```

---

[View on LeetCode](https://leetcode.com/problems/find-pivot-index/)