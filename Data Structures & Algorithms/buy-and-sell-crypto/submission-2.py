class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - mini
            mini = min(mini, prices[i])
            res = max(res,profit)
        return res
            


