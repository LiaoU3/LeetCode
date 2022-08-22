from typing import List
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        hm = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            hm[('r', r)].append(i)
            hm[('c', c)].append(i)        
        
        n = len(stones)
        state = [False] * n
        
        def dfs(i):
            if state[i]:
                return
            state[i] = True
            r, c = stones[i]
            for j in hm[('r', r)]:
                dfs(j)
            for j in hm[('c', c)]:
                dfs(j)
        cnt = 0
        for i in range(n):
            if not state[i]:
                cnt += 1
                dfs(i)
        return n - cnt

if __name__ == '__main__':
    sol = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(sol.removeStones(stones))