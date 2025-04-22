# DP solution but faster
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        lengths = []
        for word in wordDict:
            lengths.append(len(word))
        lengths.sort()
        wordSet = set(wordDict)

        for i in range(1, len(s) + 1):
            for length in lengths:
                if i - length < 0:
                    break
                if dp[i - length] and s[i - length: i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=lambda s: len(s))

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(wordDict[0]) - 1, len(dp)):
            for word in wordDict:
                if i - len(word) < 0:
                    break
                if dp[i - len(word)] and word == s[i - len(word): i]:
                    dp[i] = True
                    break

        return dp[-1]


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