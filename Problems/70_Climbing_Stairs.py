class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1
        prepre = 1
        if n == 1:
            return 1
        for _ in range(2, n+1):
            curr = pre + prepre
            prepre = pre
            pre = curr
        return curr

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]