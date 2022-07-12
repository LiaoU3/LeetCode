from functools import cache
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4:
            return False
        avg = sum(matchsticks)//4
        N = len(matchsticks)
        self.res = False
        matchsticks.sort(reverse=True)
        
        def traverse(index: int, len1: int, len2: int, len3: int, len4: int):
            if len1==len2==len3==avg:
                self.res = True
                return
            if self.res or index==len(matchsticks) or len1>avg or len2>avg or len3>avg or len4>avg:
                return
            traverse(index+1, len1+matchsticks[index], len2, len3, len4)
            # with this index>0, 1, 2 can reduce many calculation
            if index>0:
                traverse(index+1, len1, len2+matchsticks[index], len3, len4)
            if index>1:
                traverse(index+1, len1, len2, len3+matchsticks[index], len4)
            if index>2:
                traverse(index+1, len1, len2, len3, len4+matchsticks[index])
        traverse(0, 0, 0, 0, 0)
        return self.res

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