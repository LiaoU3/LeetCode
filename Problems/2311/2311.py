class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        total = 0
        bits = k.bit_length()
        cnt = 0
        for i, c in enumerate(s[::-1]):
            if c == "1":
                if i < bits and total + (1 << i) <= k:
                    total += 1 << i
                    cnt += 1
            else:
                cnt += 1
        return cnt
