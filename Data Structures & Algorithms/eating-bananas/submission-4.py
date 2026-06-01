import numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hrs = 0
            for i in piles:
                hrs = hrs + np.ceil(i / mid)
            if hrs <= h:
                res = min(res,mid)
                right = mid - 1
            else:
                left = mid + 1
        return res