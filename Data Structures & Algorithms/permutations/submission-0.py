class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtracking():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for i in range(0, len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtracking()
                subset.pop()
        backtracking()
        return res

        

        