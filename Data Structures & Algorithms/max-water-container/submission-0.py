class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            distance = right - left
            height = min(heights[left], heights[right]) 
            area = distance * height 
            res = max(res, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return res        