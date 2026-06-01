class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, each_num in enumerate(nums):
            product = 1
            for j,each_num in enumerate(nums):
                if i!=j:
                    product = product * nums[j] 
            res.append(product)
        return res         

        