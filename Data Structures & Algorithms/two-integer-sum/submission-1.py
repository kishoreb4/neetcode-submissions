class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, each_num in enumerate(nums):
            dic[each_num] = i
        for i, each_num in enumerate(nums):
            diff = target - each_num
            if diff in dic and dic[diff] != i:
                return [i, dic[diff]]
        return []    
        
        