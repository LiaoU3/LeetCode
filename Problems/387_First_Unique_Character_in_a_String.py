# another solution using built-in function, it's kinda like cheating, I suggest using my second solution
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1

# I think this is a better solution
#  class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hash_map = {}
#         for c in s:
#             if c not in hash_map:
#                 hash_map[c] = 1
#             else:
#                 hash_map[c] += 1

#         for i, c in enumerate(s):
#             if hash_map[c] == 1:
#                 return i
#         return -1