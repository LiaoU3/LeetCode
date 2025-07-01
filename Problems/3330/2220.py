class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = None
        res = 1
        cnt = 1
        for c in word:
            if c == prev:
                cnt += 1
            else:
                prev = c
                res += cnt - 1
                cnt = 1
        res += cnt - 1
        return res
