class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def check(l, r):
            if l >= r:
                return True
            if not s[l].isalnum():
                return check(l + 1, r)
            if not s[r].isalnum():
                return check(l, r - 1)
            if s[l].lower() != s[r].lower():
                return False
            return check(l + 1, r - 1)

        return check(0, len(s) - 1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             while not s[left].isalnum() and left < right:
#                 left  += 1
#             while not s[right].isalnum() and left < right:
#                 right -= 1
#             if s[left].lower() != s[right].lower():
#                 return False
#             left  += 1
#             right -= 1
#         return True


if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))