class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        res = float('inf')
        n = len(freq)

        for i in range(n):
            deletions = 0
            base = freq[i]
            for j in range(n):
                if freq[j] < base:
                    deletions += freq[j]
                elif freq[j] > base + k:
                    deletions += freq[j] - (base + k)
            res = min(res, deletions)

        return res