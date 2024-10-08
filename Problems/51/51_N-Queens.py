from typing import List

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