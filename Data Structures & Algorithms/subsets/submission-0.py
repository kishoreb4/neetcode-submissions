class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, current):
            res.append(current[:])   # record every state

            for i in range(start, len(nums)):
                current.append(nums[i])   # choose
                dfs(i + 1, current)       # explore
                current.pop()             # unchoose

        dfs(0, [])
        return res