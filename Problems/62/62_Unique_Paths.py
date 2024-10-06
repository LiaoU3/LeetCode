class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)]for j in range(m)]
        for c in range(n):
            dp[0][c] = 1
        for r in range(m):
            dp[r][0] = 1
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c-1]+dp[r-1][c]
        return dp[m-1][n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += (dp[i][j-1] if j-1 >= 0 else 0) + (dp[i-1][j] if i-1 >= 0 else 0)
        return dp[m-1][n-1]