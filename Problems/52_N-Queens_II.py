class Solution:
    def __init__(self):
        self.cnt = 0
    def totalNQueens(self, n: int) -> int:
        def checkValid(board, row, col):
            # check up
            r = row
            while r-1 >= 0:
                if board[r-1][col] == 'Q':
                    return False
                r -= 1
            
            # check diagonal
            r = row
            c = col
            while r-1 >= 0 and len(board)-1 >= c+1:
                if board[r-1][c+1] == 'Q':
                    return False
                r -= 1
                c += 1

            # check anti-diagonal
            r = row
            c = col
            while r-1 >= 0 and c-1 >= 0:
                if board[r-1][c-1] == 'Q':
                    return False
                r -= 1
                c -= 1
            return True

        def countTotal(board, row):
            for col in range(len(board)):
                if row == len(board):
                    self.cnt += 1
                    return
                else:
                    if checkValid(board, row, col):
                        board[row][col] = 'Q'
                        countTotal(board, row+1)
                        board[row][col] = '.'

        board = [['.' for _ in range(n)]for _ in range(n)]
        countTotal(board, 0)
        return self.cnt