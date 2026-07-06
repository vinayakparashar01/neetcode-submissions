class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        sorted_hm=sorted(hm.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for num, freq in sorted_hm[:k]:
            ans.append(num)
        return ans

        
        


        