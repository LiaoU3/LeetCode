class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        res = 0
        for i in range(N):
            res += fruits[i][i]
            fruits[i][i] = 0

        for r in range(N):
            for c in range(N - r - 1):
                fruits[r][c] = 0

        for r in range(N):
            for c in range(r, N):
                up = fruits[r - 1][c] if r - 1 >= 0 else 0
                up_right = fruits[r - 1][c + 1] if r - 1 >= 0 and c + 1 < N else 0
                up_left = fruits[r - 1][c - 1] if r - 1 >= 0 and c - 1 >= 0 else 0
                fruits[r][c] += max(up, up_right, up_left)
        res += fruits[N - 1][N - 1]
        fruits[N - 1][N - 1] = 0

        for i in range(N):
            fruits[i][i] = 0

        for c in range(N):
            for r in range(c, N):
                left = fruits[r][c - 1] if c - 1 >= 0 else 0
                left_up = fruits[r - 1][c - 1] if c - 1 >= 0 and r - 1 >= 0 else 0
                left_down = fruits[r + 1][c - 1] if r + 1 < N and c - 1 >= 0 else 0
                fruits[r][c] += max(left, left_up, left_down)
        res += fruits[N - 1][N - 1]
        return res
