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
            # Out of boundry
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


# TLE O(M * N * W * 4^L)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROW = len(board)
        COL = len(board[0])
        
        seen = set()
        def dfs(r, c, i, j):
            if j == len(words[i]):
                return True
            if not(0 <= r < ROW and 0 <= c < COL):
                return False
            if board[r][c] != words[i][j]:
                return False
            if (r, c) in seen:
                return False
            seen.add((r, c))
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if dfs(r + dr, c + dc, i, j + 1):
                    seen.remove((r, c))
                    return True
            seen.remove((r, c))
            return False


        res = []
        found = set()
        for r in range(ROW):
            for c in range(COL):
                for i in range(len(words)):
                    if i in found:
                        continue
                    if dfs(r, c, i, 0):
                        res.append(words[i])
                        found.add(i)
        return res

sol = Solution()
board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]

words = ["oa","oaa"]
print(sol.findWords(board, words))