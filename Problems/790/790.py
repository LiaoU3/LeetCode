# O(N)
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        mod = 10 ** 9 + 7
        curr = 0
        for i in range(3, n + 1):
            if i > 2:
                curr += dp[i - 3]
                dp[i] += 2 * curr
            dp[i] += dp[i - 1]
            dp[i] += dp[i - 2]
            dp[i] %= mod
        return dp[-1]

# O(N ** 2)
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        mod = 10 ** 9 + 7
        for i in range(3, n + 1):
            for j in range(i - 3 + 1):
                dp[i] += 2 * dp[j]
            dp[i] += dp[i - 1]
            dp[i] += dp[i - 2]
            dp[i] %= mod
        return dp[-1]