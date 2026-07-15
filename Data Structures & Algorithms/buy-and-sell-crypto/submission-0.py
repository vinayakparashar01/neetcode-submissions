class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxi=0
        while j<len(prices):
            if prices[i]>=prices[j]:
                i=j
                j=j+1
                
            else:
                cur = prices[j]-prices[i]
                maxi=max(maxi,cur)
                j+=1
        return maxi