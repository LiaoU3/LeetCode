from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["#"] = {}
        ROW = len(board)
        COL = len(board[0])
        used = set()
        res = set()
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        def dfs(r, c, curr, word):
            # Out of bounday
            if not(0 <= r < ROW and 0 <= c < COL):
                return
            # Used in current
            if (r, c) in used:
                return
            # Not the right char
            char = board[r][c]
            if char not in curr:
                return
            used.add((r, c))
            word += char
            if "#" in curr[char]:
                res.add(word)
            for dr, dc in directions:
                dfs(r + dr, c + dc, curr[char], word)
            used.remove((r, c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, trie, "")
        return list(res)

sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]

words = ["oath","pea","eat","rain"]
print(sol.findWords(board, words))