class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,num1 in enumerate(nums):
            sub_sum = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    sub_sum *= num2
            res.append(sub_sum)
        return res
      

        