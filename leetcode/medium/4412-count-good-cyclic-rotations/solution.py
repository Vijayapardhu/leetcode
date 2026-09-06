class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        half=n//2
        firstsum=sum(nums[:half])
        total=sum(nums)
        ans=0
        curr=firstsum
        for i in range(n):
            if curr>total-curr:
                ans+=1
            curr-=nums[i]
            curr+=nums[(i+half)%n]
        return ans