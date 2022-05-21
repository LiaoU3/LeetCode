import collections
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = collections.defaultdict(float('Inf'))
        dp[0] = 0
        for num in range(1, amount+1):
            dp[num] = min(dp[num-coin]for coin in coins)
        return -1 if dp[amount] == float('Inf') else dp[amount]
# BFS Solution, but it;s not fast enough
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         curr = [0]
#         count = 0
#         while curr:
#             count += 1
#             nxt = []
#             for total in curr:
#                 for coin in coins:
#                     if total + coin == amount:
#                         return count
#                     if total + coin < amount:
#                         nxt.append(total + coin)
#             curr = nxt
#         return -1

def main():
    solution = Solution()
    coins = [1]
    amount = 0
    print(solution.coinChange(coins, amount))

if __name__ == '__main__':
    main()