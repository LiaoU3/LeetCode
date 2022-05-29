from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k:
            return 0
        dp = [[-float('Inf'),  0] for _ in range(k)]
        for p in prices:
            pre_sell = 0
            for i in range(len(dp)):
                dp[i][0] = max(dp[i][0], -p + pre_sell)
                dp[i][1] = max(dp[i][1], p + dp[i][0])
                pre_sell = dp[i][1]
        return dp[-1][-1]

if __name__ =='__main__':
    sol = Solution()
    k = 2
    prices = [3,2,6,5,0,3]
    print(sol.maxProfit(k, prices))