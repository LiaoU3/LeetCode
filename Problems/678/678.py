# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_n_max = [0, 0]  # The min and max number of ')' can we currently have
        for c in s:
            if c == "(":
                min_n_max[0] += 1
                min_n_max[1] += 1
            elif c == "*":
                if min_n_max[0] > 0:
                    min_n_max[0] -= 1
                min_n_max[1] += 1
            else:
                if min_n_max[0] > 0:
                    min_n_max[0] -= 1
                min_n_max[1] -= 1
            if min_n_max[1] < 0:
                return False
        return min_n_max[0] == 0

# Wrong answer
class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        stack = []
        for c in s:
            if c == "*":
                cnt += 1
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if cnt >= len(stack):
            return True
        else:
            return False