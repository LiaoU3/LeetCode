from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - price)
            dp[i][1] = dp[i - 1][0] + price
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1][1], dp[-1][2])

s = Solution()
prices = [1,2,3,0,2]
print(s.maxProfit(prices))