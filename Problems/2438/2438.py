class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        powers = []
        bit = 1
        while n:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1

        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)

        res = []
        for start, end in queries:
            total = prefix[end + 1]
            prev = prefix[start]
            res.append(total * pow(prev, MOD - 2, MOD) % MOD)
        return res
