class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [ch for ch in s if ch.isalnum()]
        for i in range(len(s)):
            if s[i] != s[len(s) -1 - i]:
                return False
        return True
            
             