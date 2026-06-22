class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def max_money(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            if i in memo:
                return memo[i]
            memo[i] = max(max_money(i-2)+nums[i],max_money(i-1))
            return memo[i]
        return max_money(len(nums)-1)