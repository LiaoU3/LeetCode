class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_length = 0
        max_area = 0
        for x, y in dimensions:
            curr_length = x * x + y * y
            if curr_length > max_length:
                max_length = curr_length
                max_area = x * y
            elif curr_length == max_length:
                max_area = max(max_area, x * y)
        return max_area
