class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if  len(str) == 0 :
            return 0 
			
        sign = 1
        val = 0
        if str[0] in ["-", "+"]:
            sign = 1 if str[0] == '+' else -1	
            str = str[1:]

        for char in str:
            if not char.isdigit(): 
                break
            val = val * 10 + (ord(char) - ord("0"))
        return min(2**31 - 1, max(-2**31, val * sign))

### Wrong solution
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         end = 0
#         for i in range(len(s)):
#             if s[i] != ' ':
#                 if s[i] == '+' or s[i] == '-' or 47 < ord(s[i]) < 58 :
#                     start = i
#                     break
#                 else:
#                     return 0
#         for i in range(i + 1, len(s)):
#             if ord(s[start + ])
#             if ord(s[i]) > 57 or ord(s[i]) < 48 or i ==len(s) - 1:
#                 end = i
#                 break
#         return max(min(int(float(s[start:end + 1])), 2 ** 31 - 1), -2 ** 31)
solution = Solution()
s = "+-12"
print(solution.myAtoi(s))