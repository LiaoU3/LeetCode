from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0] for _ in range(len(prices))]
        # buy -> sell
        # sell -> rest
        # rest -> rest, buy
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            # buy
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            # sell
            dp[i][1] = dp[i - 1][0] + prices[i]
            # rest
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        
        return max(dp[-1])

s = Solution()
prices = [1,2,3,0,2]
print(s.maxProfit(prices))