from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(l, r):
            if l > r:
                return -1
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:  # left sorted
                if nums[l] <= target < nums[m]:
                    return binary_search(l, m - 1)
                else:
                    return binary_search(m + 1, r)
            else:  # right sorted
                if nums[m] < target <= nums[r]:
                    return binary_search(m + 1, r)
                else:
                    return binary_search(l, m - 1)

        return binary_search(0, len(nums) - 1)

if __name__ == '__main__':
    sol = Solution()
    nums = [3,1]
    target = 1
    print(sol.search(nums, target))