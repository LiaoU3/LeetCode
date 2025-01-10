# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n = len(text1)
#         m = len(text2)
#         dp = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if text1[j] == text2[i]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j] if i > 0 else 0, dp[i][j - 1] if j > 0 else 0)
#         return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for r in range(1, n):
            for c in range(1, m):
                if text1[c - 1] == text2[r - 1]:
                    dp[r][c] = dp[r - 1][c -1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]