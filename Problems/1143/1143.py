class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                else:
                    dp[i][j] = max(dp[i - 1][j] if i > 0 else 0, dp[i][j - 1] if j > 0 else 0)
        return dp[-1][-1]