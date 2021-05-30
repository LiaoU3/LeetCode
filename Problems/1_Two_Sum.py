class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            to_find_num = target - nums[i]
            if to_find_num in nums[:i] or to_find_num in nums[i+1:]:
                ans.append(i)
                ans.append(nums.index(to_find_num, i+1))
                return ans
                break
