class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2

        cache = {}
        def backtrack(i, total):
            if i == len(stones) or total >= target:
                return abs(total - (stone_sum - total))
            if (i, total) in cache:
                return cache[(i, total)]
            cache[(i, total)] = min(backtrack(i + 1, total), backtrack(i + 1, total + stones[i]))
            return cache[(i, total)]

        return backtrack(0, 0)
