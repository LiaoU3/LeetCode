class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW = len(mat)
        COL = len(mat[0])
        up = True
        r, c = 0, 0
        res = []
        for _ in range(ROW * COL):
            res.append(mat[r][c])
            if up:
                if r - 1 >= 0 and c + 1 < COL:
                    r -= 1
                    c += 1
                else:
                    up = False
                    if c + 1 < COL:
                        c += 1
                    else:
                        r += 1
            else:
                if r + 1 < ROW and c - 1 >= 0:
                    r += 1
                    c -= 1
                else:
                    up = True
                    if r + 1 < ROW:
                        r += 1
                    else:
                        c += 1
        return res
