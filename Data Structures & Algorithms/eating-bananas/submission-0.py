class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid = l+(r-l)//2
            cur = 0
            for i in piles:
                cur+=(i+mid-1)//mid
            if cur <= h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res

        
        
        