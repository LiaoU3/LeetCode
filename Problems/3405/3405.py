class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        comb = math.comb(n - 1, k)
        res = comb * m % MOD
        res *= (m - 1) ** (n - 1 - k)
        res %= MOD

        return res

# TLE
# class Solution:
#     def countGoodArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         def combination(i, j):
#             # C i get j
#             res = 1
#             for k in range(i, i - j, -1):
#                 res *= k
#             for k in range(j, 0, -1):
#                 res //= k
#             return res % MOD
#         comb = combination(n - 1, k)
#         res = comb * m % MOD
#         for _ in range(n - 1 - k):
#             res *= (m - 1)
#             res %= MOD

#         return res


sol = Solution()
n = 4
m = 2
k = 2
print(sol.countGoodArrays(n, m, k))
