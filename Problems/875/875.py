from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        def binary_search(l, r):
            if l > r:
                return l
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += p // m
                if p % m:
                    total += 1
                if total > h:
                    return binary_search(m + 1, r)
            return binary_search(l, m - 1)

        return binary_search(1, piles[0])

sol = Solution()
piles = [11]
h = 2
print(sol.minEatingSpeed(piles, h))