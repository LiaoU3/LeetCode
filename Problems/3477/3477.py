class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        res = N
        for i, f in enumerate(fruits):
            for j in range(N):
                if baskets[j] >= f:
                    res -= 1
                    baskets[j] = 0
                    break
        return res
