class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []
        stack = []
        for d in dominoes:
            if d == "L":
                if not stack:
                    res.append("L")
                else:
                    if stack[0] == ".":
                        res.append("L" * (len(stack) + 1))
                    else:
                        res.append("R" * (len(stack) // 2))
                        if len(stack) % 2 == 0:
                            res.append(".")
                        else:
                            res.append("RL")
                        res.append("L" * (len(stack) // 2))
                    stack = []
            elif d == "R":
                if stack:
                    if stack[0] == "R":
                        res.append("R" * len(stack))
                        stack = []
                    else:
                        res.extend(stack)
                        stack = []
                stack.append("R")
            else:
                stack.append(".")

        if stack:
            res.append(("R" if stack[0] == "R" else ".") * len(stack))

        return "".join(res)


dominoes = ".L.R...LR..L.."
sol = Solution()
print(sol.pushDominoes(dominoes))
