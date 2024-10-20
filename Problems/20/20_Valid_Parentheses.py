class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "}": "{",
            "]": "[",
            ")": "(",
            }
        stack = []
        for c in s:
            if stack:
                if c in parentheses:
                    if stack[-1] != parentheses[c]:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(c)
            else:
                if c in parentheses:
                    return False
                else:
                    stack.append(c)
        return True if not stack else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack:
                if c in "([{":
                    stack.append(c)
                else:
                    if stack[-1] == "(" and c == ")":
                        stack.pop()
                    elif stack[-1] == "[" and c == "]":
                        stack.pop()
                    elif stack[-1] == "{" and c == "}":
                        stack.pop()
                    else:
                        return False
            else:
                if c == ")" or c == "]" or c == "}":
                    return False
                else:
                    stack.append(c)
        return True if not stack else False

## 2 solutions below have the similar speed
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')' : '(',
                '}' : '{',
                ']' : '['}
        stack = []
        for c in s:
            if c in pair.keys():
                if len(stack)>= 1 and stack[-1] == pair[c]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                stack += c
        return stack == []

# class Solution:
#     def isValid(self, s: str) -> bool:
#         pair = {')' : '(',
#                 '}' : '{',
#                 ']' : '['}
#         stack = ''
#         for c in s:
#             stack += c
#             if c in pair.keys():
#                 if  len(stack) >= 2 and stack[-2] == pair[c]:
#                     stack = stack[:-2]
#                 else:
#                     return False
#         return True if len(stack)==0 else False

solution = Solution()
s = '[]]]]]]]]]]]]]]]]]'
print(solution.isValid(s))