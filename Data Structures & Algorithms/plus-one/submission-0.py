class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s=s+str(i)
        x=int(s)
        x+=1
        y=str(x)
        res=[]
        for j in y:
            res.append(int(j))
        return res             


        