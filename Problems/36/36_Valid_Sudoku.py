from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen_row = defaultdict(set)  # row
        seen_col = defaultdict(set)  # col
        seen_box = defaultdict(set)  # (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen_row[r]:
                    return False
                seen_row[r].add(board[r][c])

                if board[r][c] in seen_col[c]:
                    return False
                seen_col[c].add(board[r][c])

                if board[r][c] in seen_box[(r // 3, c //3)]:
                    return False
                seen_box[(r // 3, c //3)].add(board[r][c])
        return True

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