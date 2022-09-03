class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def helper(num, digit):
            if digit == n:
                res.append(num)
                return
            lastDigit = num % 10
            tmp = num
            if lastDigit + k < 10:
                tmp *= 10
                tmp += lastDigit + k
                helper(tmp, digit + 1)
            if not k:
                return
            tmp = num
            if lastDigit - k >= 0:
                tmp *= 10
                tmp += lastDigit - k
                helper(tmp, digit + 1)
        
        for i in range(1, 10):
            helper(i, 1)
        
        return res