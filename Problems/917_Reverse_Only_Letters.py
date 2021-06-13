class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        while r-l > 0:
            if s[l].isalpha() and s[r].isalpha():
                    s = s[:l] + s[r] + s[l + 1 : r] + s[l] + s[r + 1 :]
                    l += 1
                    r -= 1
            if not s[l].isalpha():
                l += 1
            if not s[r].isalpha():
                r -= 1
        return s

solution = Solution()
s = "a-bC-dEf-ghIj"
print(solution.reverseOnlyLetters(s))