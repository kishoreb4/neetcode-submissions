from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for each_num in nums:
            if each_num in dic.keys():
                return True 
            else:
                dic[each_num] = 1
        return False        