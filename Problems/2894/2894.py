# O(1)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        total = (1 + n) * n // 2

        if m > n:
            return total

        cnt = n // m
        num2 = m * cnt * (cnt + 1) // 2
        return total - num2 * 2


# O(N)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        total = sum(i for i in range(n + 1))

        num1 = 0
        for i in range(1, n + 1):
            if i % m:
                num1 += i

        return num1 * 2 - total
