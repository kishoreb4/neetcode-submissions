class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 1
        min_price = prices[0]
        while i < len(prices):
            res = max(res,prices[i] - min_price)
            min_price = min(min_price, prices[i])
            i = i + 1
        return res


        