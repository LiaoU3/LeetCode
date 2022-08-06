class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest // minutesToDie + 1
        pigs = 0
        while times ** pigs < buckets:
            pigs += 1
        return pigs