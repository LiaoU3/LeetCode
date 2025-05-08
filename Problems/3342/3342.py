class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROW = len(moveTime)
        COL = len(moveTime[0])

        hp = [(0, 1, 0, 0)]  # (time, dtime, row, col)
        visited = set()  #(row, col)
        while hp:
            time, dtime, r, c = heappop(hp)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROW - 1 and c == COL - 1:
                return time
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                    heappush(hp, (max(time, moveTime[nr][nc]) + dtime, 1 if dtime == 2 else 2, nr, nc))
