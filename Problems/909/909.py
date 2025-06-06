class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROW = len(board)
        COL = len(board[0])
        TARGET = ROW * COL

        def number2rc(num):
            num -= 1
            r = num // COL
            c = num % COL
            row = ROW - 1 - r
            if r % 2 == 1:
                c = COL - 1 - c
            return (row, c)

        visited = set()
        q = deque([(0, 1)])  # (step, num)
        visited.add(1)

        while q:
            step, num = q.popleft()
            if num == TARGET:
                return step
            for i in range(1, 7):
                nxt = num + i
                if nxt > TARGET or nxt in visited:
                    continue
                row, col = number2rc(nxt)
                visited.add(nxt)
                if board[row][col] != -1:
                    q.append((step + 1, board[row][col]))
                else:
                    q.append((step + 1, nxt))
        return -1


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROW = len(board)
        COL = len(board[0])
        hash_map = {}
        r = ROW - 1
        c = 0
        cnt = 1
        for r in range(ROW - 1, -1, -1):
            if (ROW - r) % 2:
                for c in range(COL):
                    hash_map[cnt] = (r, c)
                    cnt += 1
            else:
                for c in range(COL - 1, -1, -1):
                    hash_map[cnt] = (r, c)
                    cnt += 1

        q = deque([(1, 0)])  # num, move
        seen = set()
        while q:
                num, move = q.popleft()
                if num in seen:
                    continue
                seen.add(num)
                r, c = hash_map[num]
                if board[r][c] != -1:
                    num = board[r][c]
                if num == ROW * COL:
                    return move
                for i in range(1, 7):
                    q.append((num + i, move + 1))
        return -1