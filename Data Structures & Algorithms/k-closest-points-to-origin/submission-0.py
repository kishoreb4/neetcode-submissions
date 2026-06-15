class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = x * x + y * y
            min_heap.append((dist, [x,y]))
        heapq.heapify(min_heap)
        
        res = []
        for _ in range(k):
            _, point = heapq.heappop(min_heap)
            res.append(point)
        return res

             





        