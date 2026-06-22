class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # di = {}
        # di_t = {}
        # for i in s:
        #     di[i] = di.get(i,0) + 1
        # for i in t:
        #     di_t[i] = di_t.get(i,0) + 1    
        # for keys in di.keys():
        #     if di.get(keys,0) != di_t.get(keys,0):
        #         return False
        # for keys in di_t.keys():
        #     if di.get(keys,0) != di_t.get(keys,0):
        #         return False    
        # return True    

        return sorted(s) == sorted(t)

        