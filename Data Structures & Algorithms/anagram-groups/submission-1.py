class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            key = "".join(sorted(i))
            dic[key] = dic.get(key,[])
            dic[key].append(i)
        return list(dic.values())

        