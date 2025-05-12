class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(digits)

        res = []
        for num in range(100, 1000, 2):
            d_cnt = defaultdict(int)
            tmp = num
            while tmp:
                d_cnt[tmp % 10] += 1
                tmp //= 10
            for d, cnt in d_cnt.items():
                if cnt > counter[d]:
                    break
            else:
                res.append(num)

        return res


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        used = set()
        res = set()
        def backtrack(i, num):
            if i == 3:
                if num % 2 == 0:
                    res.add(num)
                return
            for j in range(len(digits)):
                if j in used:
                    continue
                if 0 == i == digits[j]:
                    continue
                used.add(j)
                backtrack(i + 1, num * 10 + digits[j])
                used.remove(j)

        backtrack(0, 0)

        return sorted(list(res))
