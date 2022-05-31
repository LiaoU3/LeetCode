from typing import List

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