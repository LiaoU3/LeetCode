class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        num = 0
        min_num = 0
        max_num = 0

        for diff in differences:
            num += diff
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        res = (upper - lower) - (max_num - min_num) + 1

        return res if res > 0 else 0
