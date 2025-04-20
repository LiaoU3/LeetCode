from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0
        for num, cnt in counter.items():
            if cnt > 0:
                rate = (cnt // (num + 1)) + (1 if cnt % (num + 1) else 0)
                res += rate * (num + 1)
            else:
                res += cnt
        return res


sol = Solution()
answers = [1, 1, 2]
print(sol.numRabbits(answers))
