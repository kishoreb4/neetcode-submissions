class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        un = [y for x in matrix for y in x]
        left, right = 0, len(un) - 1 
        res = []
        while left <= right:
            mid = (left + right) // 2
            if un[mid] == target:
                res.append(mid)
                break
            elif un[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return True if res else False
         