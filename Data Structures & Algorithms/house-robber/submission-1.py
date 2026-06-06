class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i == 0:
                memo[i] = nums[i]
                return nums[i]
            if i == 1:
                memo[i] = max(nums[i],nums[i-1]) 
                return max(nums[i],nums[i-1])

            if i in memo:
                return memo[i]
            else:
                skip = helper(i-1)
                take = helper(i-2) + nums[i]
                memo[i] = max(skip,take)
            return memo[i]
        return helper(len(nums) - 1)