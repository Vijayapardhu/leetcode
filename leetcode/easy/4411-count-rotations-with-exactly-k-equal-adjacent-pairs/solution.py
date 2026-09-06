class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        total_roat=0
        for i in range(n):
            if s[i] == s[(i+1)%n]:
                total_roat+=1
        if k ==total_roat:
            return n-total_roat
        if k==total_roat-1:
            return total_roat
        else:
            return 0