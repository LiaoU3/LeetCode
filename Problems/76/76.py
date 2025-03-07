from collections import defaultdict

# O(S + L)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = defaultdict(int)
        for c in t:
            target[c] += 1

        window = defaultdict(int)

        need = len(target)
        have = 0

        res = ""
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if not res or r - l + 1 < len(res):
                    res = s[l : r + 1]
                window[s[l]] -= 1
                if window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        return res


# # O (S*L)
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""

#         target = {}
#         for c in t:
#             if c not in target:
#                 target[c] = 0
#             target[c] += 1

#         window = defaultdict(int)

#         def is_legal():
#             for c in target:
#                 if target[c] > window[c]:
#                     return False
#             return True

#         res = None
#         l = 0
#         for r in range(len(s)):
#             window[s[r]] += 1
#             while is_legal():
#                 if res is None or r - l + 1 < len(res):
#                     res = s[l : r + 1]
#                 window[s[l]] -= 1
#                 l += 1

#         return res if res is not None else ""

sol = Solution()
s = "aa"
t = "aa"
print(sol.minWindow(s, t))