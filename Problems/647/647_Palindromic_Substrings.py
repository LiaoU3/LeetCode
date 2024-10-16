class Solution:
    def countSubstrings(self, s: str) -> int:

        def count_palindrome(left, right):
            cnt = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt
        count = 0
        for i in range(len(s)):
            count += count_palindrome(i, i)
            count += count_palindrome(i, i+1)
            
        return count

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        def palindrome(i):
            # Odd
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1
            
            # Even
            l = i
            r = i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            palindrome(i)
        return self.res