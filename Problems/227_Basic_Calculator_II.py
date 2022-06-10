class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        curr_num = 0
        operand  = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            if c in '+-*/' or i == len(s)-1:
                if operand == '+':
                    stack.append(curr_num)
                elif operand == '-':
                    stack.append(-curr_num)
                elif operand == '*':
                    stack[-1] *= curr_num
                else:
                    stack[-1] = int(stack[-1]/curr_num)
                curr_num = 0
                operand  = c
        
        return sum(stack)

if __name__ == '__main__':
    sol = Solution()
    s = "3+2*2"
    print(sol.calculate(s))