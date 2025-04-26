class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0

        min_index = -1
        max_index = -1

        res = 0
        l = 0
        for r, num in enumerate(nums):
            if num < minK or num > maxK:
                min_index = -1
                max_index = -1
                l = r + 1
                continue
            if num == maxK:
                max_index = r
            if num == minK:
                min_index = r
            boundary = min(min_index, max_index)
            if boundary != -1:
                res += boundary - l + 1

        return res