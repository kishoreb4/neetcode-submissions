class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for each in nums:
            if each in dic.keys():
                return True
            else:
                dic[each] = 1

        return False

    
        