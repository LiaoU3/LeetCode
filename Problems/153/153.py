class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binary_search(l, r):
            m = (l + r) // 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            elif nums[l] <= nums[m]:  # left is sorted, and right is not
                return min(nums[l], binary_search(m + 1, r))
            else:  # right is sorted', and left is not
                return min(nums[m], binary_search(l, m - 1))
        return binary_search(0, len(nums) - 1)