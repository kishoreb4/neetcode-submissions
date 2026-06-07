class Solution:
    def maxProfit(self, prices):
        memo = {}

        def dp(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + dp(i + 2, False)
                hold = dp(i + 1, True)
                memo[(i, holding)] = max(sell, hold)
            else:
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)
                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dp(0, False)