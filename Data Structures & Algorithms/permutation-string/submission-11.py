from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        n=len(s1)
        m=len(s2)
        i=0
        window =Counter(s2[0:n])
        if window==target:
                return True
        for i in range(m - n):
            window[s2[i]] -= 1
            if window[s2[i]] == 0:
                del window[s2[i]]

            window[s2[i + len(s1)]] += 1
            if window==target:
                return True
        return False

        