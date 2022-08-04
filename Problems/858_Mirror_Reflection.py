class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        def gcd(m, n):
            if n == 0:
                return m
            return gcd(n, m%n)
        
        f = gcd(p, q)
        m = p*q//f
        if (m//q) % 2 == 0:
            return 2
        else:
            if (m // p) % 2== 1:
                return 1
            else:
                return 0