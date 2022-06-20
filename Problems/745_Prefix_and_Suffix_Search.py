from typing import List

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie={}
        for index, word in enumerate(words):
            new_word = word + '#'
            length = len(new_word)
            new_word += word

            for i in range(length):
                curr = self.trie
                curr['$'] = index
                for c in new_word[i:]:
                    if c not in curr:
                        curr[c] = {}
                    curr = curr[c]
                    curr['$'] = index
    
    def f(self, prefix: str, suffix: str) -> int:
        curr = self.trie

        for c in suffix+'#'+prefix:
            if c not in curr:
                return -1
            curr = curr[c]
        return curr['$']

# TLE
# class WordFilter:
#     def __init__(self, words: List[str]):
#         self.specialDict = {}
#         for i, word in enumerate(words):
#             for j in range(1, len(word)+1):
#                 for k in range(1, j+1):
#                     for m in range(len(word)):
#                         if word[:k] + '_' + word[m:] not in self.specialDict:
#                             self.specialDict[word[:k] + '_' + word[m:]] = i
#                         else:
#                             self.specialDict[word[:k] + '_' + word[m:]] = max(i, self.specialDict[word[:k] + '_' + word[m:]])
        

#     def f(self, prefix: str, suffix: str) -> int:
#         if prefix+ '_' +suffix in self.specialDict:
#             return self.specialDict[prefix +'_'+suffix]
#         else:
#             return -1


# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(['bccbacbcba'])
print(obj.specialDict['bccbacbcba_a'])
print(obj.specialDict)