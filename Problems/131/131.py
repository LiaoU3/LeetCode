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