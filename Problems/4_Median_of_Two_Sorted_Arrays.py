class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        total = len(nums)
        index = total//2
        if total % 2 == 1:
            return float(nums[index])
        else:
            return float((nums[index] + nums[index-1])/2)