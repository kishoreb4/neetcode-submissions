# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         subset = []
#         candidates = sorted(candidates)
#         def dfs(start,total):
#             if total == target:
#                 res.append(subset[:])
#                 return
#             if total > target:
#                 return

#             for i in range(start,len(candidates)):
#                 if i > start and candidates[i] == candidates[i-1]:
#                     continue
#                 if total + candidates[i] > target:
#                     break
#                 subset.append(candidates[i])
#                 dfs(i +1, total + candidates[i])
#                 subset.pop()
#         dfs(0,0)
#         return res
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        subset = []
        def backtracking(start, total):
            if total == target:
                res.append(subset[:])
                return
            if total > target:
                return
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtracking(i + 1, total + nums[i])
                subset.pop()

        backtracking(0,0)    
        return res        
        