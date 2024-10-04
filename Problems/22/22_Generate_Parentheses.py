class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(s: str, l: int, r: int):
            if l == r == n:
                res.append(s)
                return
            if l < n:
                backtrack(s + "(", l + 1, r)
            if l > r:
                backtrack(s + ")", l, r + 1)
        backtrack("", 0, 0)
        return res
            

class Solution:
    def generateParenthesis(self, n: int) -> list:
        stack = []
        res = []
        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                res.append(''.join(stack))

            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if openCount > closeCount:
                stack.append(')')
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)
        return res

# it will miss the (())(())
# class Solution:
#     def generateParenthesis(self, n: int) -> list:
#         prev_ret, ret = ['()'], ['()']
#         for i in range(1,n):
#             ret = []
#             for element in prev_ret:
#                 prev_ret = ret
#                 ret.append('(' +element + ')')
#                 if element + '()' not in ret:
#                     ret.append(element + '()')
#                 if '()' + element not in ret:
#                     ret.append('()' + element)
#         return ret

solution = Solution()
print(solution.generateParenthesis(3))