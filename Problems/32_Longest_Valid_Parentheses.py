# Brilliant solution, but I am not the one who came up with this LOL
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_max = 0
        count_left_bracket  = 0
        count_right_bracket = 0
        for c in s:
            if c == '(':
                count_left_bracket  += 1
            else:
                count_right_bracket += 1
            if count_left_bracket == count_right_bracket:
                len_max = max(len_max, count_left_bracket+count_right_bracket)
            if count_left_bracket<count_right_bracket:
                count_left_bracket  = 0
                count_right_bracket = 0

        count_left_bracket  = 0
        count_right_bracket = 0
        for c in s[::-1]:
            if c == '(':
                count_left_bracket  += 1
            else:
                count_right_bracket += 1
            if count_left_bracket == count_right_bracket:
                len_max = max(len_max, count_left_bracket+count_right_bracket)
            if count_left_bracket>count_right_bracket:
                count_left_bracket  = 0
                count_right_bracket = 0

        return len_max


# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = []
#         len_max = 0
#         for i in range(len(s)):
#             if len(stack)>0 and  s[i]==')' and s[stack[-1]]=='(':
#                 stack.pop()
#             else:
#                 stack.append(i)

#             if len(stack) >0:
#                 len_max = max(len_max, i-stack[-1])
#             else:
#                 len_max = i+1
#         return len_max

def main():
    s = ")()())"
    sol = Solution()
    print(sol.longestValidParentheses(s))

if __name__ == '__main__':
    main()