class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                removed = []
                while stack and stack[-1] != "[":
                    removed.append(stack.pop())
                stack.pop()

                tmp = []
                while stack and stack[-1].isnumeric():
                    tmp.append(stack.pop())
                times = int("".join(tmp[::-1]))

                stack.extend(removed[::-1] * times)

        return "".join(stack)


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


s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
sol = Solution()
print(sol.decodeString(s))
