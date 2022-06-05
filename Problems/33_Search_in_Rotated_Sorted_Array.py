from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target = target
        nums   = nums

        def binary_search(left, right):
            if left > right:
                return -1
            middle = (left + right)//2
            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    return binary_search(left, middle-1)
                else:
                    return binary_search(middle+1, right)
            else:
                if nums[middle] < target <= nums[right]:
                    return binary_search(middle+1, right)
                else:
                    return binary_search(left, middle-1)
        
        return binary_search(0, len(nums)-1)

if __name__ == '__main__':
    sol = Solution()
    nums = [3,1]
    target = 1
    print(sol.search(nums, target))