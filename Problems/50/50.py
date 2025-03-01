# O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x * x, n // 2)
            return res * x if n & 1 else res

        res = helper(x, abs(n))
        return res if n > 0 else 1 / res

# TLE but cleaner solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n >= 0 else 1 / res

# TLE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        if n > 0:
            for i in range(n):
                res *= x
        if n < 0:
            for i in range(-n):
                res /= x
        return res
