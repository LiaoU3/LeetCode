from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                word1 = set(words[i])
                word2 = set(words[j])
                if len(word1.intersection(word2)) == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product