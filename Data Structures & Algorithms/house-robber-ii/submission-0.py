class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
    
        # Case 1: exclude last house (rob 0 to n-2)
        case1 = self.rob_linear(nums[0:-1])
        
        # Case 2: exclude first house (rob 1 to n-1)
        case2 = self.rob_linear(nums[1:])
        
        return max(case1, case2)

    def rob_linear(self,nums):    
        res = []
        i = 0
        
        while i < len(nums):
            if i == 0:
                
                res.append(nums[0])
            elif i == 1:
                
                res.append(max(nums[0],nums[1]))
            else:
        
                res.append(max(nums[i]+res[i-2],res[i-1]))
            i = i + 1
        return res[-1]