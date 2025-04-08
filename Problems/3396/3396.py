from typing import List
from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        remain = 0
        for num in nums:
            cnt[num] += 1
            if cnt[num] == 2:
                remain += 1
        if remain == 0:
            return 0

        res = 0
        i = 0
        while remain > 0:
            res += 1
            for j in range(3):
                if i < len(nums):
                    cnt[nums[i]] -= 1
                    if cnt[nums[i]] == 1:
                        remain -= 1
                i += 1
        return res


nums = [5, 7, 11, 12, 12]
sol = Solution()
print(sol.minimumOperations(nums))
