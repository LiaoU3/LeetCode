# DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                start = i - len(word) + 1
                if start < 0:
                    continue
                if (start == 0 or dp[start - 1]) and s[start: i + 1] == word:
                    dp[i] = True
                    break  # Since we have make sure that it is valid at least until s[i-1]
        return dp[-1]


# TLE Solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        def dfs(s):
            if not s:
                self.res = True
                return
            for word in wordDict:
                if word == s[:len(word)]:
                    dfs(s[len(word):])
        dfs(s)
        return self.res