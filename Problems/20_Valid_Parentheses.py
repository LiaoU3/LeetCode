class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')' : '(',
                '}' : '{',
                ']' : '['}
        stack = ''
        for c in s:
            stack += c
            if c in pair.keys():
                if  len(stack) >= 2 and stack[-2] == pair[c]:
                    stack = stack[:-2]
                else:
                    return False
        return True if len(stack)==0 else False

solution = Solution()
s = ']'
print(solution.isValid(s))