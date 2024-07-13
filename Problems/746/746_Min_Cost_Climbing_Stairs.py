class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2:i]) + cost[i]
        return min(dp[-1], dp[-2])

# without using additional space
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         cost += [0]
#         for i in range(2, len(cost)):
#             cost[i] = cost[i] + min(cost[i-1], cost[i-2])
#         return cost[-1]

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         cost += [0]
#         dp = [0]*(len(cost))
#         dp[0] = cost[0]
#         dp[1] = cost[1]
#         for i in range(2, len(dp)):
#             dp[i] = cost[i] + min(dp[i-1], dp[i-2])
#         return dp[-1]