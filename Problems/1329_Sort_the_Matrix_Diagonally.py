class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        hm = defaultdict(list)
        for i in range(m):
            for j in range(n):
                heappush(hm[i-j], mat[i][j])
        for i in range(m):
            for j in range(n):
                mat[i][j] = heappop(hm[i-j])
        return mat            