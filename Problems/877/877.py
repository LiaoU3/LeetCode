class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)

        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            left = piles[l] + dfs(l + 1, r)
            right = piles[r] + dfs(l, r - 1)
            cache[(l, r)] = min(left, right)
            return cache[(l, r)]

        return 2 * dfs(0, len(piles) - 1) > total


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
