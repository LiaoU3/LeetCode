from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = 10 ** 9 + 7
        dp = {}
        total = 0
        for i, father in enumerate(arr):
            dp[father] = 1
            for j in range(i):
                child = arr[j]
                # we don't have to check the child bigger than the square root of father
                if child > father **0.5:
                    break
                # not divisible or not inside the dp
                if father % child or father // child not in dp:
                    continue
                if child == father // child:
                    dp[father] += dp[child] * dp[child]
                else:
                    dp[father] += dp[child] * dp[father // child] * 2
            dp[father] %= mod
            total += dp[father]
            total %= mod
        return total

if __name__ == '__main__':
    sol = Solution()
    arr = [2,4]
    print(sol.numFactoredBinaryTrees(arr))