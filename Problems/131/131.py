class Solution:
    def partition(self, s: str) -> List[List[str]]:

        cache = {}  # key:(l, r), val: bool

        def is_pal(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                cache[(l, r)] = False
            else:
                cache[(l, r)] = is_pal(l + 1, r - 1)
            return cache[(l, r)]
        res = []
        curr = []
        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
            for j in range(i, len(s)):
                if is_pal(i, j):
                    curr.append(s[i: j + 1])
                    backtrack(j + 1)
                    curr.pop()

        backtrack(0)
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, curr):
            if i == len(s):
                res.append(curr.copy())
            for j in range(i + 1, len(s) + 1):
                if isPal(s[i:j]):
                    curr.append(s[i: j])
                    backtrack(j, curr)
                    curr.pop()
        def isPal(sub):
            l = 0
            r = len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        backtrack(0, [])
        return res
