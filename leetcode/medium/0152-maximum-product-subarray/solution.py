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