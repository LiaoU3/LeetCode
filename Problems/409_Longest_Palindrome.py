class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphaCountTable = [0]*58
        for c in s:
            alphaCountTable[ord(c)-ord('a')] += 1
        res = 0
        haveOdd = False
        for cnt in alphaCountTable:
            if cnt %2 == 1:
                haveOdd = True
                res += cnt-1
            else:
                res += cnt
        return res+1 if haveOdd else res

if __name__ == '__main__':
    sol = Solution()
    s = "abccccdd"
    print(sol.longestPalindrome(s))