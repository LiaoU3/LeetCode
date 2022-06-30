class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            remain = n&1
            res |= remain
            n >>= 1
        return res