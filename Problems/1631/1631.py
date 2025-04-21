# Time Complexity: O(R * C * log(R * C))
# Space Complexity: O(R * C)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW = len(heights)
        COL = len(heights[0])

        seen = set()
        hp = [(0, 0, 0)]
        res = 0
        while hp:
            effort, r, c = heappop(hp)
            seen.add((r, c))
            res = max(res, effort)
            if r == ROW - 1 and c == COL - 1:
                return res
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in seen:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    heappush(hp, (diff, nr, nc))
