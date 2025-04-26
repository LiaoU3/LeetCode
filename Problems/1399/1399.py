class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = 0
            while i:
                digit_sum += i % 10
                i //= 10
            sums[digit_sum] += 1
        max_cnt = max(sums.values())

        res = 0
        for cnt in sums.values():
            if cnt == max_cnt:
                res += 1

        return res