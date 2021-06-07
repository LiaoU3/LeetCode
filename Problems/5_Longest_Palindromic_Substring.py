class Solution:
	def longestPalindrome(self, s):
		if len(s)==0:
			return 0
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

# solution = Solution()
# print(solution.longestPalindrome('babdasspddggp'))