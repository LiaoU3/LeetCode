class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                string = ""
                ch = stack.pop()
                while ch.isalpha():
                    string = ch+string
                    ch = stack.pop()
                num = ""
                ch = stack.pop()
                while ch.isnumeric():
                    num = ch+num
                    if stack and stack[-1].isnumeric():
                        ch = stack.pop()
                    else:
                        break
                num = int(num)
                stack.append(string*num)
        return ''.join(stack)

if __name__ == '__main__':
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s))