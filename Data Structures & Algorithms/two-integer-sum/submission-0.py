class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        n=len(nums)
        for i in range(n):
            key = target - nums[i]
            if key in hm:
                return [hm[key],i]
            hm[nums[i]]=i    

        