# make a set record calculated num, get rid of duplicated calculation
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        currs = [n]
        count = 0
        seen = set()
        while currs:
            nxts = []
            for curr in currs:
                for square_num in squares:
                    left_num = curr-square_num
                    if left_num in seen:
                        continue
                    if left_num<0:
                        break
                    if left_num > 0:
                        seen.add(left_num)
                        nxts.append(left_num)
                    else:
                        return count+1
            currs = nxts
            count += 1

# pure BFS Solution without dp
# class Solution:
#     def numSquares(self, n: int) -> int:
#         squares = [i**2 for i in range(1, int(n**0.5)+1)]
        
#         currs = [n]
#         count = 0
#         while currs:
#             nxts = []
#             for curr in currs:
#                 for square_num in squares:
#                     if curr-square_num > 0:
#                         nxts.append(curr-square_num)
#                     elif curr-square_num == 0:
#                         return count+1
#                     else:
#                         break
#             currs = nxts
#             count += 1

if __name__ == "__main__":
    sol = Solution()
    n = 12
    print(sol.numSquares(n))