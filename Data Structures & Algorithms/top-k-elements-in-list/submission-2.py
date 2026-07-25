from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        sorted_d = sorted(d.items(),key=lambda x:x[1])
        top_k = sorted_d[-k:]  
        return [a for a,b in top_k]

        