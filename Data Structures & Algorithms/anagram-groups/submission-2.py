class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = "".join(sorted(s))
            res[key] = res.get(key,[])
            res[key].append(s)
        return list(res.values())
        