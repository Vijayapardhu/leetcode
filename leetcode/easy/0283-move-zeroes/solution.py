class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero_found_at = 0
        
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap elements to move non-zero to the front and zeroes to the back
                nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1