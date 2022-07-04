from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price-buy)
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ret = 0
#         curr_min = float('Inf')
#         for p in prices:
#             ret = max(ret, p - curr_min)
#             curr_min = min(curr_min, p)
#         return ret

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = [0 for _ in range(len(prices))]
#         # pre_price = prices[0]
#         for i in range(1, len(prices)):
#             add = dp[i-1] + prices[i] - prices[i-1]
#             dp[i] = add if add>0 else 0
#         return max(dp)

if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))