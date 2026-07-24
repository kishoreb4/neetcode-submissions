class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis = []
        for num in nums:
            if num in lis:
                return True
            else:
                lis.append(num)
        return False 

        