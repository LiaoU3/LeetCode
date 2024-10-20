# Best Solution using set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        res = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return len(s)
        left = 0
        maxLen = 1
        lastSeen = [-1]*95
        for right in range(len(s)):
            c = s[right]
            left = max(left, lastSeen[ord(c)-32]+1)
            lastSeen[ord(c)-32] = right
            maxLen = max(maxLen, right-left+1)
        return maxLen


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