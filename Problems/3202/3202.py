from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mods = [0] * k
        for num in nums:
            new_mods = [0] * k
            num %= k
            for i in range(k):
                j = (i - num + k) % k
                new_mods[j] = max(mods[j], mods[i] + 1)
            mods = new_mods
        return max(mods)


nums = [1,4,2,3,1,4]
k = 3
sol = Solution()
print(sol.maximumLength(nums, k))
