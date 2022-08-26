class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        n = sorted(str(N))
        for i in range(32):
            x = 2**i
            m = sorted(str(x))
            if m == n: 
                return True
        return False