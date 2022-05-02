# fastest solution
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        cnt = 0
        for i in set(s):
            if s.count(i)%2 != 0:
                cnt+=1 
        return False if cnt > k else True

# second fast solution
# class Solution:
#     def canConstruct(self, s: str, k: int) -> bool:
#         if len(s) < k:
#             return False
#         c_dict = {}
#         for c in s:
#             if c not in c_dict:
#                 c_dict[c] = 1
#             else:
#                 c_dict[c] += 1
#         cnt = 0
#         for c in c_dict.keys():
#             if c_dict[c] % 2 == 1:
#                 cnt +=1
#         return False if cnt > k else True

# slow solution 
# class Solution:
#     def canConstruct(self, s: str, k: int) -> bool:
#         if len(s) < k:
#             return False
#         num_set = set()
#         for c in s:
#             if c not in num_set:
#                 num_set.add(c)
#             else:
#                 num_set.remove(c)
#         if len(num_set) > k:
#             return False
#         return True

def main():
    solution = Solution()
    s = "annabelle"
    k = 2
    print(solution.canConstruct(s, k))

if __name__ =='__main__':
    main()