class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)
        for i in range(0,k):
            res = heapq.heappop(nums)
        return -res
        