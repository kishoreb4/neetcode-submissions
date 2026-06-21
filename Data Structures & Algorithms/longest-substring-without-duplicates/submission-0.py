class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        i = 1
        ls = [s[0]]
        while i < len(s):
            if s[i] not in ls:
                ls.append(s[i])
                res = max(res,len(ls))
            else:
                while s[i] in ls:
                    ls.pop(0)
                ls.append(s[i])
                res = max(res,len(ls))
            i = i + 1
        return res


        