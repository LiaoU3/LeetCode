class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        len_max = 0
        for i in range(len(s)):
            if len(stack)>0 and  s[i]==')' and s[stack[-1]]=='(':
                stack.pop()
            else:
                stack.append(i)

            if len(stack) >0:
                len_max = max(len_max, i-stack[-1])
            else:
                len_max = i+1
        return len_max

def main():
    s = "()"
    sol = Solution()
    print(sol.longestValidParentheses(s))

if __name__ == '__main__':
    main()