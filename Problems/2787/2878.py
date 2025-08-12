class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        powers = []
        for i in range(1, n + 1):
            if i ** x > n:
                break
            powers.append(i ** x)

        dp = [0] * (n + 1)
        dp[0] = 1
        for power in powers:
            for i in range(n - power, -1, -1):
                dp[i + power] += dp[i]
                dp[i + power] %= MOD
        return dp[-1]
