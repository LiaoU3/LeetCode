from typing import List

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         candies = [1]*len(ratings)
#         for i in range(1, len(ratings)):
#             if ratings[i]>ratings[i-1]:
#                 candies[i] = candies[i-1]+1
#         for i in range(len(ratings)-2, -1, -1):
#             if ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
#                 candies[i] = candies[i+1]+1
#         return sum(candies)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        cnt = 0
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                if cnt:
                    candies[i] = 2
                    candies[i-1] = 1
                    for j in range(i-1, i-cnt-2, -1):
                        if ratings[j]>ratings[j+1] and candies[j]<=candies[j+1]:
                            candies[j] = candies[j+1]+1
                        elif ratings[j]>ratings[j+1] and candies[j]<=candies[j+1]:
                            candies[j] = 1
                    cnt = 0
                else:
                    candies[i] = candies[i-1]+1
            elif ratings[i]==ratings[i-1]:
                candies[i] = 1
            else:
                cnt += 1

        if cnt:
            candies[i] = 1
            for j in range(i-1, i-cnt-1, -1):
                if ratings[j]>ratings[j+1] and candies[j]<=candies[j+1]:
                    candies[j] = candies[j+1]+1
                elif ratings[j]>ratings[j+1] and candies[j]<=candies[j+1]:
                    candies[j] = 1
            cnt = 0
        print(ratings)
        print(candies)
        return sum(candies)
                
if __name__ == '__main__':
    sol = Solution()
    ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
    print(sol.candy(ratings))