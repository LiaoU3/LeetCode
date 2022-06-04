from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def checkValid(board, row, col):
            # check col
            r = row
            while r-1 >= 0:
                if board[r-1][col] == 'Q':
                    return False
                r -= 1

            # check diagonal
            r = row
            c = col
            while len(board)-1 >= c+1 and r-1 >= 0: 
                if board[r-1][c+1] == 'Q':
                    return False
                c += 1
                r -= 1

            # check anti-diagonal
            r = row
            c = col
            while c-1 >= 0 and r-1 >= 0: 
                if board[r-1][c-1] == 'Q':
                    return False
                c -= 1
                r -= 1
            
            return True

        res = []

        def solve(board, row):
            for col in range(len(board)):
                if row == len(board):
                    res.append([''.join(r) for r in board])
                    return
                elif row < len(board):
                    if checkValid(board, row, col):
                        board[row][col] = 'Q'
                        solve(board, row+1)
                        board[row][col] = '.'
                else:
                    return

        board = [['.'for _ in range(n)] for _ in range(n)] 
        solve(board, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.solveNQueens(n))