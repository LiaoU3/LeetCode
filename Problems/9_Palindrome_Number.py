## Faster solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or(x>0 and x%10 ==0):
            return False
        else:
            rev = 0
            while x > rev:
                rev = rev*10 + x % 10
                x = x//10
            return rev == x or rev//10 == x
## This solution is not fast enough !
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         if x[0] == '-':
#             return False
#         else:
#             if x[::-1] == x:
#                 return True