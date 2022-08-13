from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hm = defaultdict(int)
        for word in words:
            hm[word] += 1
        
        total = 0        
        same = False
        for word, cnt1 in hm.items():
            if word[0]==word[1]:
                total += (cnt1//2) * 4
                if cnt1 % 2:
                    same = True
            else:
                if word[::-1] not in hm:
                    continue
                cnt2 = hm[word[::-1]]
                used =  min(cnt1, cnt2)
                hm[word] -= used
                hm[word[::-1]] -= used
                total += used* 4
        return total + 2 if same else total


if __name__ == '__main__':
    sol = Solution()
    words = ["lc","cl","gg"]
    print(sol.longestPalindrome(words))