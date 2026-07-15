from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q=deque()
        maxi=0
        for i in s:
            while i in q:
                q.popleft()
            q.append(i)
            maxi=max(maxi,len(q))
        return maxi

        