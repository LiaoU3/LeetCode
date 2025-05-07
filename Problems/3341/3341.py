class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        ROW = len(moveTime)
        COL = len(moveTime[0])

        visited = set()  #(row, col)
        hp = [(0, 0, 0)]  # (time, row, col)

        while hp:
            time, row, col = heappop(hp)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == ROW - 1 and col == COL - 1:
                return time
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr = row + dr
                nc = col + dc
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                    heappush(hp, ((max(time, moveTime[nr][nc]) + 1, nr, nc)))
