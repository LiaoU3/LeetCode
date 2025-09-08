class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def has_zero(num: int) -> bool:
            while num:
                if num % 10 == 0:
                    return True
                num //= 10
            return False
        
        for i in range(1, n // 2 + 1):
            if not has_zero(i) and not has_zero(n - i):
                return [i, n - i]
