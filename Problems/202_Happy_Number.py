class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        
        while True:
            total = 0
            while n:
                total += (n % 10)**2
                n //= 10
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total