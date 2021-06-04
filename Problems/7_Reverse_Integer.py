class Solution:
    def reverse(self, x: int) -> int:
        limit = pow(2, 31)
        x = str(x)
        if x[0] == '-':
            return -int(x[:0:-1]) if -int(x[:0:-1]) > -limit else 0
        else:
            return int(x[::-1]) if int(x[::-1])  < limit - 1 else 0
solution = Solution()
print(solution.reverse(-123))