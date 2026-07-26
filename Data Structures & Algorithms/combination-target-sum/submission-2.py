class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(start,total):
            if total == target:
                res.append(subset[:])
                return
            if total > target:
                return    

            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i,total + nums[i])
                subset.pop()


        dfs(0,0)
        return res


    

        