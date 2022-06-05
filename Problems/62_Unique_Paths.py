class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += (dp[i][j-1] if j-1 >= 0 else 0) + (dp[i-1][j] if i-1 >= 0 else 0)
        return dp[m-1][n-1]