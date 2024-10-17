from collections import defaultdict


# Not fast enough
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        def satisfied():
            for c in target:
                if target[c] > 0:
                    return False
            return True
        res = ""
        l = 0
        for r in range(len(s)):
            if s[r] in target:
                target[s[r]] -= 1
                while satisfied():
                    if not res or len(res) > r - l + 1:
                        res = s[l:r + 1]
                    if s[l] in target:
                        target[s[l]] += 1
                    l += 1
        return res

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s, t))