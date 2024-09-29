# This is problem is not suitable to solve by Python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        if not b:
            return a if a <= MAX_INT else ~(a ^ MASK)
        nxt_a = (a ^ b) & MASK
        nxt_b = ((a & b) << 1) & MASK
        return self.getSum(nxt_a, nxt_b)