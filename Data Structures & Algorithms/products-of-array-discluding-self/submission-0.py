class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        l=[1]*n
        m=[1]*n
        cur=1
        for i in range(1,n):
            l[i]=cur*nums[i-1]
            cur=l[i]
        cur=1    
        for j in range(n-1,-1,-1):
            if j-1 <0:
                break
            m[j-1]=nums[j]*cur
            cur=m[j-1]
        res=[1]*n
        for k in range(n):
            res[k]=l[k]*m[k]
        return res        






        