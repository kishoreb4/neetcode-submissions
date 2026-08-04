class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        inter = []
        for i in range(0,len(s)):
            if s[i] not in inter:
                inter.append(s[i])
                res = max(res,len(inter))
            else:
                while (s[i] in inter):
                    inter.pop(0)
                inter.append(s[i])
        return res