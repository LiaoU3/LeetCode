class Solution:
    def kthCharacter(self, k: int) -> str:
        res = [0]
        while len(res) <= k:
            nxt = res.copy()
            for i in range(len(nxt)):
                nxt[i] += 1
            res.extend(nxt)
        return chr(ord("a") + (res[k - 1] % 26))