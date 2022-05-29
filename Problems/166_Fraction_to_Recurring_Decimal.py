class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        remainders = {}
        ret = ""
        while True:
            if numerator >= denominator:
                remain = numerator%denominator
                ret += str(numerator//denominator)
                if remain in remainders:
                    ret = ret[:remainders[numerator]] + '(' + ret[remainders[numerator]:] + ')'
                    break
                remainders[remain] = len(ret)

                numerator = remain*10
            else:
                numerator *= 10
                if not ret:
                    ret = "0."
                else:
                    ret += '0'

            if numerator == 0:
                break
                
        return ret

if __name__ == '__main__':
    numerator = 4
    denominator = 333
    sol = Solution()
    print(sol.fractionToDecimal(numerator, denominator))