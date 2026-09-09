class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position=bisect_left(nums, target)
        last_position=bisect_right(nums,target)
        if first_position == last_position:
            return [-1,-1]
        else:
            return [first_position, last_position-1]