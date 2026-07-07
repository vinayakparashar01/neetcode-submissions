class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for i in numset:
            cur=1
            if (i-1) not in numset:
                while i+cur in numset:
                    cur+=1
            longest=max(cur,longest)  
        return longest          

        