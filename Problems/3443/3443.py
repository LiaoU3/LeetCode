class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        res = 0
        for c in s:
            counter[c] += 1
            dist = abs(counter["N"] - counter["S"]) + abs(counter["E"] - counter["W"])
            dist += 2 * min(k, min(counter["N"], counter["S"]) + min(counter["E"], counter["W"]))
            res = max(res, dist)
        return res
