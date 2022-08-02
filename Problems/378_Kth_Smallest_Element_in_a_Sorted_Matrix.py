from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp = [float('-Inf')]*k
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                heapq.heappushpop(hp, -matrix[i][j])
        return -hp[0]

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(sol.kthSmallest(matrix, k))