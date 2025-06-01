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
        i = 0
        while nums[i] != -1:
            nxt = nums[i]
            nums[i] = -1
            i = nxt
        return i

# O(N*log(N))
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


sol = Solution()
nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))