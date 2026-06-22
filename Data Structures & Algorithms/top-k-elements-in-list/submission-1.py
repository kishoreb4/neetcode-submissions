class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for i in nums:
            di[i] = di.get(i,0) + 1
        freq = [[] for _ in range(len(nums) + 1)] 
        for num, cnt in di.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
