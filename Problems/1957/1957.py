class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = []
        for i in range(min(2, len(s))):
            res.append(s[i])
        for c in s[2::]:
            if c == res[-1] == res[-2]:
                continue
            res.append(c)
        return "".join(res)
