class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = [0] * 26
        MOD = 10 ** 9 + 7
        for c in s:
            counter[ord(c) - ord("a")] += 1

        for _ in range(t):
            new_counter = [0] * 26
            for i, cnt in enumerate(counter[:-1]):
                new_counter[i + 1] += cnt
                new_counter[i + 1] %= MOD
            new_counter[0] += counter[-1]
            new_counter[0] %= MOD
            new_counter[1] += counter[-1]
            new_counter[1] %= MOD
            counter = new_counter

        return sum(counter) % MOD