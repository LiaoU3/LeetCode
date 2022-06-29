class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            if n==1:
                return True
            if n%2==1:
                return False
            n //= 2
        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n!=0 and n&(n-1)==0 else False