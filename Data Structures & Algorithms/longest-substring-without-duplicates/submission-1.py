from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q=deque()
        seen=set()
        maxi=0
        for i in s:
            while i in seen:
                x = q.popleft()
                seen.remove(x)
            q.append(i)
            seen.add(i)
            maxi=max(maxi,len(q))
        return maxi

        