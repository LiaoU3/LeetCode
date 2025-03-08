# Cleaner solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #   a b  (s)
        # .
        # *
        #(p)

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*" and dp[i - 2][0]:
                dp[i][0] = True

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i - 2][j] or ((p[i - 2] == s[j - 1] or p[i - 2] == ".") and dp[i][j - 1])
                elif p[i - 1] == "." or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #   a b  (s)
        # .
        # *
        #(p)

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*" and dp[i - 2][0]:
                dp[i][0] = True

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if dp[i - 1][j - 1]:
                    if p[i - 1].isalpha() and p[i - 1] == s[j - 1]:
                        dp[i][j] = True
                        continue
                    elif p[i - 1] == ".":
                        dp[i][j] = True
                        continue
                    elif p[i - 1] == "*" and s[j - 1] == p[i - 2]:
                        dp[i][j] = True
                        continue
                if dp[i - 1][j]:
                    if p[i - 1] == "*":
                        dp[i][j] = True
                        continue
                if dp[i][j - 1]:
                    if p[i - 1] == "*" and (p[i - 2] == "." or s[j - 1] == p[i - 2]):
                        dp[i][j] = True
                        continue
                if dp[i - 2][j]:
                    if p[i - 1] == "*":
                        dp[i][j] = True
                        continue
        return dp[-1][-1]

sol = Solution()
s = "aaa"
p = "ab*ac*a"
print(sol.isMatch(s, p))