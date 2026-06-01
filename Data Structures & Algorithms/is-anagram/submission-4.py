class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}
        for each_char in s:
            dic_s[each_char] = dic_s.get(each_char,0) + 1
        for each_char in t:
            dic_t[each_char] = dic_t.get(each_char,0) + 1    
        return dic_s == dic_t
        
            