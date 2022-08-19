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

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = nums[0]
        localMin = nums[0]
        globalMax = nums[0]
        print(localMin, localMax, globalMax)
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                localMax, localMin = max(num, localMin * num), min(num, localMax * num)
            else:
                localMax, localMin = max(num, localMax * num), min(num, localMin * num)
            globalMax = max(globalMax, localMax)
            print(localMin, localMax, globalMax)
        return globalMax