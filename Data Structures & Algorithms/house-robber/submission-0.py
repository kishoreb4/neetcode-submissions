class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 0
        res = []
        while i < len(nums):
            if i == 0:
                res.append(nums[0])
            elif i == 1:
                res.append(max(nums[0],nums[1]))
            else:
                res.append(max((res[i-2]+nums[i]), (res[i-1]))) 
            i = i + 1       
        return res[len(nums) - 1]
        