class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0 for _ in range(n)]  for _ in range(5)]
        for i in range(5):
            dp[i][0] = 1
        for i in range(1, n):
            dp[0][i] = (dp[1][i-1] + dp[2][i-1] + dp[4][i-1]) % mod
            dp[1][i] = (dp[0][i-1] + dp[2][i-1]) % mod
            dp[2][i] = (dp[1][i-1] + dp[3][i-1]) % mod
            dp[3][i] = dp[2][i-1]
            dp[4][i] = (dp[2][i-1] + dp[3][i-1]) % mod
        
        total = 0
        for i in range(5):
            total = (total + dp[i][n-1]) % mod
        return total