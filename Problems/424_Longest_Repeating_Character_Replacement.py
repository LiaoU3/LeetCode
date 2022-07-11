class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = [0]*26
        currMaxCnt = 0
        maxLen = 0
        l = 0
        for r in range(len(s)):
            table[ord(s[r])-ord('A')] += 1
            currMaxCnt = max(currMaxCnt, table[ord(s[r])-ord('A')])
            while r-l+1-currMaxCnt>k:
                table[ord(s[l])-ord('A')]-= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen                