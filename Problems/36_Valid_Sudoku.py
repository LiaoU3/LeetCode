from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        box_seen = defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = board[row][col] 
                if curr != '.':
                    if curr in row_seen[row] or curr in col_seen[col] or curr in curr in box_seen[row//3, col//3]:
                        return False
                    row_seen[row].add(curr)
                    col_seen[col].add(curr)
                    box_seen[row//3, col//3].add(curr)
        return True

def main():
    solution = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    print(solution.isValidSudoku(board))

if __name__ == '__main__':
    main()