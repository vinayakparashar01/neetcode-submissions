class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        s.add(n)
        while True:
            summ=0
            for i in str(n):
                summ=summ+(int(i)**2)
            if summ==1:
                return True
            if summ in s:
                return False
            s.add(summ)
            n=summ

        