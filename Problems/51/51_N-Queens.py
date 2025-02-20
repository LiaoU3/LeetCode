from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        used_rows = set()  # r
        used_cols = set()  # c
        used_main_diagonal = set()  # r - c 
        used_anti_diagonal = set()  # r + c

        def coord2board(coord):
            board = [["." for _ in range(n)] for _ in range(n)]
            for r, c in coord:
                board[r][c] = "Q"
            for r in range(n):
                board[r] = "".join(board[r])
            return board

        res = []
        def backtrack(curr):
            if len(curr) == n:
                res.append(coord2board(curr))
                return
            r = len(curr)
            for c in range(n):
                if c in used_cols or (r - c) in used_main_diagonal or (r + c) in used_anti_diagonal:
                    continue
                used_cols.add(c)
                used_main_diagonal.add(r - c)
                used_anti_diagonal.add(r + c)
                curr.append((r, c))
                backtrack(curr)
                used_cols.remove(c)
                used_main_diagonal.remove(r - c)
                used_anti_diagonal.remove(r + c)
                curr.pop()        
        backtrack([])

        return res

# Faster
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c
        board = [["."] * n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col:
                    continue
                if (r + c) in pos_diag:
                    continue
                if (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
        
#         def checkValid(board, row, col):
#             # check col
#             r = row
#             while r-1 >= 0:
#                 if board[r-1][col] == 'Q':
#                     return False
#                 r -= 1

#             # check diagonal
#             r = row
#             c = col
#             while len(board)-1 >= c+1 and r-1 >= 0: 
#                 if board[r-1][c+1] == 'Q':
#                     return False
#                 c += 1
#                 r -= 1

#             # check anti-diagonal
#             r = row
#             c = col
#             while c-1 >= 0 and r-1 >= 0: 
#                 if board[r-1][c-1] == 'Q':
#                     return False
#                 c -= 1
#                 r -= 1
            
#             return True

#         res = []

#         def solve(board, row):
#             for col in range(len(board)):
#                 if row == len(board):
#                     res.append([''.join(r) for r in board])
#                     return
#                 elif row < len(board):
#                     if checkValid(board, row, col):
#                         board[row][col] = 'Q'
#                         solve(board, row+1)
#                         board[row][col] = '.'
#                 else:
#                     return

#         board = [['.'for _ in range(n)] for _ in range(n)] 
#         solve(board, 0)
#         return res

if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.solveNQueens(n))