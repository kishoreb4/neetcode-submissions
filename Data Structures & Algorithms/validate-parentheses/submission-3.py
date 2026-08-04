class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',
                '}':'{',
                ']' : '['}
        lis = []
        i = 0
        while i < len(s):
            if s[i] in dic.keys():
                if len(lis) > 0:
                    if lis[-1] != dic[s[i]]:
                        return False
                    else: 
                        lis.pop()
                else:
                    return False
            else:
                lis.append(s[i])
            i += 1
        return len(lis) == 0

