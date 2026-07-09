class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        s=s.lower()
        for i in s:
            if i.isalnum():
                str+=i
            else:
                continue
        return str==str[::-1]        

        