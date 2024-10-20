# Time complexity O(N), Space Complexity O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr = 1
        for i in range(1, len(nums)):
            res[i] = curr * nums[i - 1]
            curr *= nums[i - 1]
        curr = 1
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= curr * nums[i + 1]
            curr *= nums[i + 1]
        return res

# Time complexity O(N), Space Complexity O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [0] * len(nums)
        l2r[0] = 1
        r2l = [0] * len(nums)
        r2l[-1] = 1
        for i in range(1, len(nums)):
            l2r[i] = l2r[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            r2l[i] = r2l[i + 1] * nums[i + 1]

        res = [r2l[0]]
        for i in range(1, len(nums) - 1):
            res.append(l2r[i] * r2l[i])
        res.append(l2r[-1])
        return res