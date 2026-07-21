from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=0
        n=len(s1)
        m=len(s2)
        while j<m:
            j=i+n
            if Counter(s1)==Counter(s2[i:j]):
                return True
            i+=1
        return False
        