from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                j = i - num
                if j < 0:
                    break
                dp[i] += dp[j]
        return dp[-1]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[-1]

# TLE
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         self.count = 0
        
#         def helper(currNums):
#             if sum(currNums) > target:
#                 return
#             if sum(currNums) == target:
#                 self.count += 1
#                 return
#             for num in nums:
#                 helper(currNums + [num])
#         helper([])
#         return self.count

if __name__ == '__main__':
    sol = Solution()
    nums =     [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111]
    target =     999
    print(sol.combinationSum4(nums, target))