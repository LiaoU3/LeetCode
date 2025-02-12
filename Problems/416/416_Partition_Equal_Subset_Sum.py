class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        nums.sort()
        half = total / 2
        dp = set([0])
        for num in nums:
            new_dp = set()
            for n in dp:
                if n + num == half:
                    return True
                new_dp.add(n + num)
            dp = new_dp | dp
        return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        dp = [False]*(target+1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] |= dp[i-num]
        return dp[-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        self.res = False
        seen = set()  # memorize it
        def backtrack(curr, total, i):
            if self.res:
                return
            if i == len(nums):
                return
            if total == target:
                self.res = True
                return
            if total > target:
                return
            if (total, i) in seen:
                return
            seen.add((total, i))
            backtrack(curr, total, i + 1)
            curr.append(i)
            backtrack(curr, total + nums[i], i + 1)

        backtrack([], 0, 0)
        return self.res


# TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        self.res = False
        def backtrack(curr, total, i):
            if self.res:
                return
            if i == len(nums):
                return
            if total == target:
                self.res = True
                return
            if total > target:
                return
            backtrack(curr, total, i + 1)
            curr.append(i)
            backtrack(curr, total + nums[i], i + 1)

        backtrack([], 0, 0)
        return self.res