class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm={}
        maxf=0
        maxlen=0
        j=0
        for r in range(len(s)):
            hm[s[r]]=hm.get(s[r],0)+1
            maxf=max(maxf,hm[s[r]])
            while (r-j+1) - maxf > k :
                hm[s[j]]-=1
                j+=1
            maxlen=max(maxlen,r-j+1)
        return maxlen





