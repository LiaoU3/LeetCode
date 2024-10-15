from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1  = buy2  = -float('Inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1  = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2  = max(buy2, -p + sell1)
            sell2 = max(sell2, p + buy2)
        return sell2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            dp[i][0] = max(dp[i - 1][0], -price)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + price)
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - price)
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + price)
        return dp [-1][3]

# Cannot buy and sell at the same time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        hp = [0, 0]
        for i in range(1, len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            else:
                heappush(hp, prices[i] - smallest)
                heappop(hp)
        return sum(hp)

if __name__ =='__main__':
    sol = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(sol.maxProfit(prices))