class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in the wordList, there is no way we could find it in it
        if endWord not in wordList:
            return 0
        hash_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                hash_map[pattern].append(word)
        qu = deque([beginWord])
        res = 1
        visited = set([beginWord])
        while qu:
            for _ in range(len(qu)):
                word_source = qu.pop()
                if word_source == endWord:
                    return res
                for i in range(len(word_source)):
                    pattern = word_source[:i] + "*" + word_source[i + 1:]
                    for word_target in hash_map[pattern]:
                        if word_target in visited:
                            continue
                        qu.appendleft(word_target)
                        visited.add(word_target)
            res += 1
        return 0

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def diff_only_one(s1, s2):
#             cnt = 0
#             for c1, c2, in zip(s1, s2):
#                 if c1 != c2:
#                     cnt += 1
#                 if cnt > 1:
#                     return False
#             return True if cnt else False
#         wordList = set(wordList)            
#         qu = deque([beginWord])
#         res = 1
#         while qu:
#             length = len(qu)
#             res += 1
#             for _ in range(length):
#                 word_source = qu.pop()
#                 to_be_removed = []
#                 for word_target in wordList:
#                     if diff_only_one(word_source, word_target):
#                         qu.appendleft(word_target)
#                         to_be_removed.append(word_target)
#                         if word_target == endWord:
#                             return res
#                 for word in to_be_removed:
#                     wordList.remove(word)
#         return 0