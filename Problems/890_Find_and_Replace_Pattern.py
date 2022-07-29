from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        tableW = [-1]*26
        tableP = [-1]*26
        res = []
        for word in words:
            for i, c in enumerate(word):
                if tableW[ord(c)-ord('a')] != -1 and tableW[ord(c)-ord('a')] != ord(pattern[i])-ord('a'):
                    break
                tableW[ord(c)-ord('a')] = ord(pattern[i])-ord('a')
                if  tableP[ord(pattern[i])-ord('a')] != -1 and tableP[ord(pattern[i])-ord('a')] != ord(c)-ord('a'):
                    break
                tableP[ord(pattern[i])-ord('a')] = ord(c)-ord('a')
            else:
                res.append(word)
            tableP = [-1]*26
            tableW = [-1]*26
        return res

if __name__ == '__main__':
    words = ["abc","cba","xyx","yxx","yyx"]
    pattern = "abc"
    # pattern = "abb"
    sol = Solution()
    print(sol.findAndReplacePattern(words, pattern))