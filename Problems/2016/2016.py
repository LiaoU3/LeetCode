class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        seen_min = float("Inf")
        for num in nums:
            res = max(res, num - seen_min)
            seen_min = min(seen_min, num)
        return res if res > 0 else -1
