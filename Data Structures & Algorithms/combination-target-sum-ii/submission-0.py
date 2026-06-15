class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates = sorted(candidates)
        def dfs(start,total)->None:
            if total == target:
                res.append(path[:])
            if total > target:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, no need to continue if already too large
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()
        dfs(0,0)
        return res

        