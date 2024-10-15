from typing import List


# Sliding window (2 pointers) solution
# Space complexity: O(1)
# Time complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = float('inf')
#         profit = 0
#         for price in prices:
#             buy = min(buy, price)
#             profit = max(profit, price-buy)
#         return profit

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

# TLE
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i, price in enumerate(prices[:-1]):
#             buy = price
#             sell = max(prices[i+1:])
#             profit = max(profit, sell - buy)
#         return profit


if __name__ == '__main__':
    sol = Solution()
    prices = [2, 1]
    print(sol.maxProfit(prices))
