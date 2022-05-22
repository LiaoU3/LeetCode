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