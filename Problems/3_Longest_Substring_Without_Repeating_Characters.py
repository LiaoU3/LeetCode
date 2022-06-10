#### Best Solition (using hashtable and slidingwindow)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0
        for w in s:
            while w in sub_str:
                sub_str = sub_str[1:]
            sub_str += w
            max_len = max(max_len, len(sub_str))
        
        return max_len

# sol = Solution()
# print(sol.lengthOfLongestSubstring("loddktdji"))


######### Better Solution (with set)    ####################
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
#         used_c = set()
#         while max_length < len(s):
#             for i in range(len(s)):
#                 if s[i] not in used_c:
#                     used_c.add(s[i])
#                 else:
#                     if len(used_c) > max_length:
#                         max_length = len(used_c)
#                     used_c = set()
#                     break
#             start = s.index(s[i]) + 1
#             s = s[start:]
#         return max(max_length ,len(used_c))


#########   Bad Solution (with list)    #################
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
#         used_c = []
#         while max_length < len(s):
#             for i in range(len(s)):
#                 if s[i] not in used_c:
#                     used_c.append(s[i])
#                 else:
#                     if len(used_c) > max_length:
#                         max_length = len(used_c)
#                     used_c = []
#                     break
#             start = s.index(s[i]) + 1
#             s = s[start:]
#         return max(max_length ,len(used_c))