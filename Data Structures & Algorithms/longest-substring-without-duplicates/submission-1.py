class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
                res = max(res, right - left + 1)
                
            char_index[s[right]] = right
            res = max(res, right - left + 1)
        return res

        # if len(s) == 0:
        #     return 0
        # res = 1
        # i = 1
        # ls = [s[0]]
        # while i < len(s):
        #     if s[i] not in ls:
        #         ls.append(s[i])
        #         res = max(res,len(ls))
        #     else:
        #         while s[i] in ls:
        #             ls.pop(0)
        #         ls.append(s[i])
        #         res = max(res,len(ls))
        #     i = i + 1
        # return res


        