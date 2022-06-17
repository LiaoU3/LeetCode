from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right = len(nums)-1
        while left<=right:
            middle = (right + left)//2
            if target == nums[middle]:
                return middle
            elif target<nums[middle]:
                right = middle-1
            else:
                left = middle+1
        return -1

if __name__=='__main__':
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    # target = 9
    print(sol.search(nums, target))