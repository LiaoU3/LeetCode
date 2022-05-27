from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        # pre_price = prices[0]
        for i in range(1, len(prices)):
            add = dp[i-1] + prices[i] - prices[i-1]
            dp[i] = add if add>0 else 0
        return max(dp)