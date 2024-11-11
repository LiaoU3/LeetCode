class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        upper_boud = 2 ** 31 - 1
        lower_bound = 2 ** 31
        is_negative = True if x < 0 else False
        if is_negative:
            x = -x
        while x:
            d = x % 10
            x //= 10
            res *= 10
            res += d
            if is_negative and (res > upper_boud // 10 or res == upper_boud) and x:
                return 0
            if not is_negative and (res > lower_bound // 10 or res == lower_bound) and x:
                return 0
        if is_negative:
            res = -res
        return res


# Cannot cover the sutiation over the boundary
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


# Cannot cover the sutiation over the boundary
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_negative = True if x < 0 else False
        if is_negative:
            x = -x
        while x:
            d = x % 10
            x //= 10
            res *= 10
            res += d
        if is_negative:
            res = -res
        return res