# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min = max(0, left_min - 1)
                left_max -= 1
            else:
                left_min = max(0, left_min - 1)
                left_max += 1
            if left_max < 0:
                return False
        return left_min == 0

# O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:

        left = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while star and left and star[-1] > left[-1]:
            star.pop()
            left.pop()
        return len(left) == 0


# TLE O(3**N)
class Solution:
    def checkValidString(self, s: str) -> bool:

        def backtrack(i, stack):
            if i == len(s):
                return len(stack) == 0
            for j in range(i, len(s)):
                if s[j] == "(":
                    stack.append(s[j])
                elif s[j] == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                else:
                    # ""
                    if backtrack(j + 1, stack.copy()):
                        return True
                    # (
                    if backtrack(j + 1, stack.copy() + ["("]):
                        return True
                    # )
                    if stack and stack[-1] == "(":
                        stack_ = stack.copy()
                        stack_.pop()
                        if backtrack(j + 1, stack_):
                            return True
            return len(stack) == 0

        return backtrack(0, [])

# Wrong answer
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         cnt = 0
#         stack = []
#         for c in s:
#             if c == "*":
#                 cnt += 1
#             elif c == ")":
#                 if stack and stack[-1] == "(":
#                     stack.pop()
#                 else:
#                     stack.append(c)
#             else:
#                 stack.append(c)
#         if cnt >= len(stack):
#             return True
#         else:
#             return False