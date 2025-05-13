class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = [0] * 26
        MOD = 10 ** 9 + 7
        for c in s:
            counter[ord(c) - ord("a")] += 1

        for _ in range(t):
            new_counter = [0] * 26
            for i, cnt in enumerate(counter[:-1]):
                new_counter[i + 1] += cnt
                new_counter[i + 1] %= MOD
            new_counter[0] += counter[-1]
            new_counter[0] %= MOD
            new_counter[1] += counter[-1]
            new_counter[1] %= MOD
            counter = new_counter

        return sum(counter) % MOD

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [[0] * 26 for _ in range(t + 1)]
        MOD = 10 ** 9 + 7
        for c in s:
            dp[0][ord(c) - ord("a")] += 1

        for i in range(1, t + 1):
            for j in range(1, 26):
                dp[i][j] = dp[i - 1][j - 1]
                dp[i][j] %= MOD
            dp[i][0] += dp[i - 1][-1]
            dp[i][0] %= MOD
            dp[i][1] += dp[i - 1][-1]
            dp[i][1] %= MOD

        return sum(dp[-1]) % MOD
