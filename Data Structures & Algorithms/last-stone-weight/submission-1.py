class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones] 
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                pass
            else:
                new = first-second
                heapq.heappush(stones,new)            
        return -stones[0] if stones else 0
        