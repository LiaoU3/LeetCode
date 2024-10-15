class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * (2 * k) for _ in range(len(prices))]
        # Not hold, buy1, sell1, buy2, sell2, ...
        for i in range(0, 2 * k, 2):
            dp[0][i] = -prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            dp[i][0] = max(dp[i - 1][0], -price)
            for j in range(1, 2 * k):
                # Sell
                if j % 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + price)
                # Buy
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - price)
        return dp[-1][-1]