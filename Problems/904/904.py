class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        types = 0
        res = 0
        cnt = 0
        l = 0
        for r in range(0, len(fruits)):
            counter[fruits[r]] += 1
            if counter[fruits[r]] == 1:
                types += 1
            cnt += 1
            while types > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    types -= 1
                l += 1
                cnt -=1
            res = max(res, cnt)
        return res
