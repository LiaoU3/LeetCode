class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        for c in range(len(s) + 1):
            dp[0][c] = 1
        for r in range(1, len(t) + 1):
            for c in range(1, len(s) + 1):
                if t[r - 1] == s[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + dp[r][c - 1]
                else:
                    dp[r][c] = dp[r][c - 1]
        return dp[-1][-1]


sol = Solution()
s = "rabbbit"
t = "rabbit"
print(sol.numDistinct(s, t))
