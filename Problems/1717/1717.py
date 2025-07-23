class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def get_score(s, pattern, point):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == pattern[0] and c == pattern[1]:
                    stack.pop()
                    score += point
                else:
                    stack.append(c)
            return score, "".join(stack)

        if x > y:
            score1, s = get_score(s, "ab", x)
            score2, _ = get_score(s, "ba", y)
        else:
            score1, s = get_score(s, "ba", y)
            score2, _ = get_score(s, "ab", x)
        return score1 + score2

# TLE
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         cache = {}
#         def dfs(s):
#             if s in cache:
#                 return cache[s]
#             max_score = 0
#             for i in range(len(s) - 1):
#                 if s[i: i + 2] == "ab":
#                     max_score = max(max_score, x + dfs(s[:i] + s[i + 2:]))
#                 elif s[i: i + 2] == "ba":
#                     max_score = max(max_score, y + dfs(s[:i] + s[i + 2:]))
#             cache[s] = max_score
#             return max_score
#         return dfs(s)
