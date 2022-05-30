class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend<0) ^ (divisor<0):
            sign = -1
        else:
            sign = 1

        if dividend<0:
            dividend = -dividend
        if divisor<0:
            divisor = -divisor

        ret = 0

        while dividend>=divisor:
            temp = divisor
            cnt = 1
            while dividend>=temp<<1:
                temp = temp<<1
                cnt  = cnt<<1
            ret += cnt
            dividend -= temp
        if sign*ret < -2**31:
            return -2^31
        if sign*ret > 2**31-1:
            return 2**31-1
        return sign*ret

if __name__ =='__main__':
    dividend = -2147483648
    divisor = -1
    sol = Solution()
    print(sol.divide(dividend, divisor))