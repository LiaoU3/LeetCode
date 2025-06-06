class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def get_longest_pal(l, r):
            if l < 0 or len(s) <= r:
                return ""
            if s[l] != s[r]:
                return ""
            curr = s[l: r + 1]
            nxt = get_longest_pal(l - 1, r + 1)
            return nxt if len(nxt) > len(curr) else curr

        for i in range(len(s)):
            pal = get_longest_pal(i, i)
            if len(pal) > len(res):
                res = pal
            pal = get_longest_pal(i, i + 1)
            if len(pal) > len(res):
                res = pal

        return res

class Solution:
	def longestPalindrome(self, s):
		maxLen=1
		start=0
		# ans = ''
		for i in range(len(s)):
			if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
				start=i-maxLen-1
				maxLen+=2
				# ans = s[start:start+maxLen]
				continue

			if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
				start=i-maxLen
				maxLen+=1
				# ans = s[start:start+maxLen]
		return s[start:start+maxLen]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check(i):
            # Odd
            l = r = i
            pal = ""
            while 0 <= l and r < len(s) and s[l] == s[r]:
                pal = s[l: r + 1]
                l -= 1
                r += 1

            # Even
            l = i
            r = i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(pal):
                    pal = s[l:r + 1]
                l -= 1
                r += 1
            return pal
        res = ""
        for i in range(len(s)):
            pal = check(i)
            if len(pal) > len(res):
                res = pal
        return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         self.s = s
#         max_len_left = 0
#         max_len_right = 0
#         max_len = 1
#         i = 0
#         for i in range(len(s)):
#             middle = i
#             left = middle
#             right = middle+1
#             while left>=0 and right<len(s) and s[left]==s[right]:
#                 if right-left+1>max_len:
#                     max_len = right-left+1
#                     max_len_left  = left
#                     max_len_right = right
#                 left  -= 1
#                 right += 1

#             left  = middle-1
#             right = middle+1
#             while left>=0 and right<len(s) and s[left]==s[right]:
#                 if right-left+1>max_len:
#                     max_len = right-left+1
#                     max_len_left  = left
#                     max_len_right = right
#                 left  -= 1
#                 right += 1
#             i += 1        
#         return s[max_len_left:max_len_right+1]

solution = Solution()
print(solution.longestPalindrome('babdasspddggp'))