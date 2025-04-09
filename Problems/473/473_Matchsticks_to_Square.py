from functools import cache
from typing import List

# Cleaner solution with cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        matchsticks.sort(reverse=True)

        cache = set()
        side = [0] * 4
        def backtrack(i):
            if i == len(matchsticks):
                return True
            if (i, side[0], side[1], side[2], side[3]) in cache:
                return False
            for j in range(4):
                side[j] += matchsticks[i]
                if side[j] <= target:
                    if backtrack(i + 1):
                        return True
                side[j] -= matchsticks[i]
            cache.add((i, side[0], side[1], side[2], side[3]))
            return False
        return backtrack(0)

# Caching could make it faster
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        matchsticks.sort(reverse=True)

        cache = set()
        def backtrack(i, p1, p2, p3, p4):
            if (i, p1, p2, p3, p4) in cache:
                return False
            if i == len(matchsticks):
                return p1 == p2 == p3 == p4
            num = matchsticks[i]
            if num + p1 <= target:
                if backtrack(i + 1, p1 + num, p2, p3, p4):
                    return True
                cache.add((i + 1, p1 + num, p2, p3, p4))
            if num + p2 <= target:
                if backtrack(i + 1, p1, p2 + num, p3, p4):
                    return True
                cache.add((i + 1, p1, p2 + num, p3, p4))
            if num + p3 <= target:
                if backtrack(i + 1, p1, p2, p3 + num, p4):
                    return True
                cache.add((i + 1, p1, p2, p3 + num, p4))
            if num + p4 <= target:
                if backtrack(i + 1, p1, p2, p3, p4 + num):
                    return True
                cache.add((i + 1, p1, p2, p3, p4 + num))
            cache.add((i, p1, p2, p3, p4))
            return False
        return backtrack(0, 0, 0, 0, 0)


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        matchsticks.sort(reverse=True)

        def backtrack(i, p1, p2, p3, p4):
            if i == len(matchsticks):
                return p1 == p2 == p3 == p4
            num = matchsticks[i]
            if num + p1 <= target:
                if backtrack(i + 1, p1 + num, p2, p3, p4):
                    return True
            if num + p2 <= target:
                if backtrack(i + 1, p1, p2 + num, p3, p4):
                    return True
            if num + p3 <= target:
                if backtrack(i + 1, p1, p2, p3 + num, p4):
                    return True
            if num + p4 <= target:
                if backtrack(i + 1, p1, p2, p3, p4 + num):
                    return True
            return False
        return backtrack(0, 0, 0, 0, 0)

# I think using cache it's kinda like cheating
# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         if sum(matchsticks)%4:
#             return False
#         avg = sum(matchsticks)//4
#         N = len(matchsticks)
#         self.res = False
#         matchsticks.sort(reverse=True)
        
#         @cache
#         def traverse(index: int, len1: int, len2: int, len3: int, len4: int):
#             if self.res or index==matchsticks or len1>avg or len2>avg or len3>avg or len4>avg:
#                 return
#             if len1==len2==len3==avg:
#                 self.res = True
#                 return
#             traverse(index+1, len1+matchsticks[index], len2, len3, len4)
#             traverse(index+1, len1, len2+matchsticks[index], len3, len4)
#             traverse(index+1, len1, len2, len3+matchsticks[index], len4)
#             traverse(index+1, len1, len2, len3, len4+matchsticks[index])
            
#         traverse(0, 0, 0, 0, 0)
#         return self.res
if __name__ == '__main__':
    sol = Solution()
    matchsticks = [1,1,2,3,3,2,4]
    print(sol.makesquare(matchsticks))