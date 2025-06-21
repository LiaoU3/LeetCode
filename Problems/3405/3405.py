class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        def combination(i, j):
            # C i get j
            res = 1
            for k in range(i, j, -1):
                res *= k
            for k in range(j, 0, -1):
                res //= k
            return res % MOD

        res = combination(n - 1, k) * m % MOD
        for _ in range(n - 1 - k):
            res *= (m - 1)
            res %= MOD 

        return res

sol = Solution()
n = 3
m = 2
k = 1
print(sol.countGoodArrays(n, m, k))