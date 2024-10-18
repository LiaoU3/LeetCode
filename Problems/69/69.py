class Solution:
    def mySqrt(self, x: int) -> int:
        
        def binary_search(l, r):
            if l > r:
                return r
            m = (l + r) // 2
            square = m ** 2
            if square == x:
                return m
            elif square > x:
                return binary_search(l, m - 1)
            else:
                return binary_search(m + 1, r)
        return binary_search(0, x)