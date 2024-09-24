class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new_n = 0
            while n:
                new_n += (n%10) ** 2
                n //= 10
            n = new_n
        return True

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = {n}
        
#         while True:
#             total = 0
#             while n:
#                 total += (n % 10)**2
#                 n //= 10
#             if total == 1:
#                 return True
#             if total in seen:
#                 return False
#             seen.add(total)
#             n = total