from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        n = len(nums)
        for i in range(n-2):
            left  = i + 1
            right = n - 1
            while left < right:
                sumUp = nums[i] + nums[left] + nums[right]
                if sumUp == target:
                    return target
                elif sumUp > target:
                    right -= 1
                else:
                    left += 1
                
                if abs(sumUp - target) < abs(closest - target):
                    closest = sumUp
        return closest


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,1]
    target = 4
    print(sol.threeSumClosest(nums, target))