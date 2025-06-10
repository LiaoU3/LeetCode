class Solution:
    def maxDifference(self, s: str) -> int:
        table = [0] * 26
        for c in s:
            table[ord(c) - ord("a")] += 1
        min_even = float("Inf")
        max_odd = -float("Inf")
        for i in range(26):
            if table[i] == 0:
                continue
            if table[i] % 2:
                max_odd = max(max_odd, table[i])
            else:
                min_even = min(min_even, table[i])
        return max_odd - min_even
