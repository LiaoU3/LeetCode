class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = [[-1, -1] for _ in range(26)]
        for i, c in enumerate(s):
            j = ord(c) - ord("a")
            if alpha[j][0] == -1:
                alpha[j][0] = i
            else:
                alpha[j][1] = i
        start = 0
        res = []
        for i in range(len(s)):
            for c in alpha:
                if c[0] <= i < c[1]:
                    break
            else:
                res.append(i - start + 1)
                start = i + 1
        return res
