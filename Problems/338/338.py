# Time Complexity O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0:      0,
        # 1:      1,
        # 2 - 3:  1, 2,
        # 4 - 7:  1, 2, 2, 3,
        # 8 - 15: 1, 2, 2, 3, 2, 3, 3, 4
        res = [0] * (n + 1)
        lookback = 1
        for i in range(1, n + 1):
            if lookback * 2 == i:
                lookback = i
            res[i] = res[i - lookback] + 1
        return res

# Time Complexity O(N*log(N))
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = []
#         for i in range(n + 1):
#             cnt = 0
#             while i:
#                 cnt += i % 2
#                 i //= 2
#             res.append(cnt)
#         return res