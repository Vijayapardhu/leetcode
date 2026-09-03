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