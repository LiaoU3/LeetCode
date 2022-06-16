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