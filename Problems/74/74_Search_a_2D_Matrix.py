class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        length = m * n
        def binarySearch(left, right):
            if left > right:
                return False
            middle = (left + right) // 2
            row = middle // n
            col = middle % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return binarySearch(left, middle - 1)
            else:
                return binarySearch(middle + 1, right)
        return binarySearch(0, length-1)