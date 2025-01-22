class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if c == "+":
                    num = num1 + num2
                elif c == "-":
                    num = num1 - num2
                elif c == "*":
                    num = num1 * num2
                else:
                    num = int(num1 / num2)
                stack.append(num)
            else:
                stack.append(int(c))
        return stack[0]
