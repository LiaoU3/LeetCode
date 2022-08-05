from typing import List

# Two pointer Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        m = len(nums)
        res = []
        for i in range(m-2):
            # if the nums[i] is bigger than 0 then nums[r] and nums[l] will definitely bigger than 0
            if nums[i] > 0:
                break
            l  = i + 1
            r  = m - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                sumUp = nums[i] + nums[l] + nums[r]
                if sumUp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # actually we just have to update l to a different nums, so we don't have to change r
                    # while l < r and nums[r] == nums[r-1]:
                        # r -= 1
                    l += 1
                    r -= 1
                elif sumUp > 0:
                    r -= 1
                else:
                    l += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        pre_i = 10**5+1
        for i in range(len(nums)-2):
            if nums[i] == pre_i:
                continue
            pre_i = nums[i]
            l = i+1
            r = len(nums)-1
            remain = -nums[i]

            while l<r:
                if nums[l] + nums[r] == remain:
                    if [nums[i], nums[l], nums[r]] not in ret:
                        ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                elif nums[l] + nums[r] > remain:
                    r -= 1
                else:
                    l += 1
        return ret
if __name__ == '__main__':
    nums = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
    sol = Solution()
    print(sol.threeSum(nums))