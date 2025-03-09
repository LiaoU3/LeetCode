from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            for _ in range(2):
                fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow


# Time Complexity O(N), Space Complexity O(N) (including the nums we modified)
# Hence, the solution is illegal to the problem.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        while nums[curr] != -1:
            res = nums[curr]
            tmp = nums[curr]
            nums[curr] = -1
            curr = tmp
        return res

sol = Solution()
nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))