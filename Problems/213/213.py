class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        nums1 = [0, 0, 0] + nums[:-1]
        nums2 = [0, 0, 0] + nums[1:]

        dp1 = [0] * (len(nums) + 2)
        dp2 = [0] * (len(nums) + 2)

        for i in range(3, len(nums1)):
            dp1[i] = max(dp1[i - 2], dp1[i - 3]) + nums1[i]
            dp2[i] = max(dp2[i - 2], dp2[i - 3]) + nums2[i]

        return max(dp1[-2:] + dp2[-2:])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(1, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        if len(nums) == 2:
            return max(dp1)
        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[-2], dp2[-1])