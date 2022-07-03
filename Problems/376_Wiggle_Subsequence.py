class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = 1
        curr = nums[0]
        start = True
        bigger = False
        # -1: down, 0: nope, 1: up
        state = 0
        for i in range(1, len(nums)):
            diff = nums[i]-curr
            if state == 0:
                if diff>0:
                    curr = nums[i]
                    dp[i] = dp[i-1]+1
                    state = 1
                elif diff<0:
                    curr = nums[i]
                    dp[i] = dp[i-1]+1
                    state = -1
                else:
                    dp[i] = dp[i-1]
            elif state == 1:
                if diff>0:
                    curr = nums[i]
                    dp[i] = dp[i-1]
                elif diff<0:
                    curr = nums[i]
                    dp[i] = dp[i-1]+1
                    state = -1
                else:
                    dp[i] = dp[i-1]
            else:
                if diff>0:
                    curr = nums[i]
                    dp[i] = dp[i-1]+1
                    state = 1
                elif diff<0:
                    curr = nums[i]
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]