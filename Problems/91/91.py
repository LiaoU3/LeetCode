class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            j = i - 1
            c = s[j]
            num = int(s[j - 1: j + 1])
            if int(c) == 0:
                if int(s[j - 1]) and num <= 26:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                total = dp[i - 1]
                if int(s[j - 1]) and num <= 26:
                    total += dp[i-2]
                dp[i] = total
        return dp[-1]


s = "10011"
sol = Solution()
print(sol.numDecodings(s))
