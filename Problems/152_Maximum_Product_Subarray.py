class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = localMin = maxProduct = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                localMax, localMin = localMin, localMax
            localMax = max(localMax*nums[i], nums[i])
            localMin = min(localMin*nums[i], nums[i])
            maxProduct = max(maxProduct, localMax)
        return maxProduct