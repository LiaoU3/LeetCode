class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        num = 1
        while num <= n:
            if num & n:
                cnt += 1
            num <<= 1
        return cnt

# Operation in bits would make it run faster

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n-1
            cnt += 1
        return cnt

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         cnt = 0
#         while n>0:
#             n = n&n-1
#             cnt += 1
#         return cnt

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         cnt = 0
#         while n>0:
#             if n%2 == 1:
#                 cnt += 1
#             n = n//2
#         return cnt