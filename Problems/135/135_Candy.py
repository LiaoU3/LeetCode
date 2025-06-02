from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        cnt = 0
        pre = res = 1
        for i in range(1, len(ratings)):
            if ratings[i]>=ratings[i-1]:
                if cnt:
                    res += cnt*(cnt+1)//2
                    if cnt >= pre:
                        res += cnt - pre + 1
                    cnt = 0
                    pre = 1
                if ratings[i]>ratings[i-1]:
                    pre += 1  
                else:
                    pre = 1
                res += pre
            else:
                cnt += 1
        if cnt:
            res += cnt*(cnt+1)//2
            if cnt >= pre:
                res += cnt - pre + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    ratings = [1,3,2,2,1]
    print(sol.candy(ratings))