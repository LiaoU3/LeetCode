from typing import List

# A clearer solution
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda word: len(word))
        hash_map = {}
        for word in words:
            curr_length = 1
            for i in range(len(word)):
                string = word[:i] + word[i+1:]
                if string in hash_map:
                    curr_length = max(curr_length, hash_map[string]+1)
                hash_map[word] = curr_length
        return max(hash_map.values())


# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         words.sort(key = lambda word: len(word))
#         hash_map = {}
#         max_len = 1
#         for word in words:
#             flag = True
#             for i in range(len(word)):
#                 string = word[:i] + word[i+1:]
#                 if string in hash_map:
#                     hash_map[word] = hash_map[string] + 1
#                     max_len = max(max_len, hash_map[word])
#                     flag = False
#             if flag:
#                 hash_map[word] = 1
#         return max_len