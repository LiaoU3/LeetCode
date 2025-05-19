class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]
        for c, b in zip(words[1:], groups[1:]):
            if b != prev:
                res.append(c)
                prev = b
        return res
