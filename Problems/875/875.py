from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        def check(k):
            time = 0
            for pile in piles:
                time += pile // k
                time += 1 if pile % k else 0
                if time > h:
                    return False
            return True

        def binary_search(l, r):
            if l > r:
                return l
            m = (l + r) // 2
            if check(m):
                return binary_search(l, m - 1)
            else:
                return binary_search(m + 1, r)

        return binary_search(1, piles[0])

sol = Solution()
piles = [11]
h = 2
print(sol.minEatingSpeed(piles, h))