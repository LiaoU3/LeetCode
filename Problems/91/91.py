class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        def check_decode(s) -> bool:
            if len(s) == 1 and s != "0":
                return True
            if len(s) == 2:
                if s[0] == "1":
                    return True
                if s[0] == "2" and s[1] in "0123456":
                    return True
            return False

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if check_decode(s[i - 2: i]):
                dp[i] += dp[i - 2]
            if check_decode(s[i - 1: i]):
                dp[i] += dp[i - 1]
            if dp[i] == 0:
                return 0
        return dp[-1]

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


# TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.res = 0

        def backtrack(i):
            if i == len(s):
                self.res += 1
                return
            if s[i] == "0":
                return
            backtrack(i + 1)
            if i + 1 < len(s) and int(s[i: i + 2]) < 27:
                backtrack(i + 2)

        backtrack(0)

        return self.res


s = "10011"
sol = Solution()
print(sol.numDecodings(s))
