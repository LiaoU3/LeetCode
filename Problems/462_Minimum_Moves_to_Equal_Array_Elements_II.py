class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()                        
        median = nums[len(nums) // 2]      
        steps = 0 
        for number in nums: 
            steps += abs(mid - number) 
        
        return steps     

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2==1:
            middle = len(nums)//2
            median = nums[middle]
        else:
            middle = len(nums)//2
            median = round((nums[middle] + nums[middle-1])/2)
        moves = 0
        for num in nums:
            moves += abs(num-median)
        return moves