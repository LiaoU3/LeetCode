class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROW = len(points)
        COL = len(points[0])

        dp = [[-float("Inf")] * COL for _ in range(ROW)]
        dp[0] = points[0]

        for r in range(1, ROW):
            seen_max = -float("Inf")
            for c in range(COL):
                seen_max = max(seen_max - 1, dp[r - 1][c])
                dp[r][c] = max(dp[r][c], seen_max)

            for c in range(COL - 1, -1, -1):
                seen_max = max(seen_max - 1, dp[r - 1][c])
                dp[r][c] = max(dp[r][c], seen_max)

            for c in range(COL):
                dp[r][c] += points[r][c]

        return max(dp[-1])
