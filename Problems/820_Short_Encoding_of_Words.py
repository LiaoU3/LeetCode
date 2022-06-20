from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted([word[::-1] for word in set(words)])
        pre_word = ""
        length = 1
        for word in words:
            if not word.startswith(pre_word):
                length += len(pre_word)+1
            pre_word = word
        return length + len(words[-1])

if __name__ == '__main__':
    sol = Solution()
    words = ["time","me","bell"]
    print(sol.minimumLengthEncoding(words))