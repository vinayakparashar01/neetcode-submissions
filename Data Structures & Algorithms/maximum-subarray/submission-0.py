class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        asum=0
        maxi=float('-inf')
        for i in nums:
            asum+=i
            if asum>maxi:
                maxi=asum
            if asum<0:
                asum=0
        return maxi

        