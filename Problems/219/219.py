class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(min(k, len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        for i in range(k, len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            seen.remove(nums[i - k])

        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i

        return False