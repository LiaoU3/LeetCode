# Cleaner solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0] * 26
        l = 0
        res = 0
        for r in range(len(s)):
            window[ord(s[r]) - ord("A")] += 1
            total = r - l + 1
            max_c = max(window)
            if total - max_c > k:
                window[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = [0 for _ in range(26)]
        l = r = res = 0
        while r < len(s):
            char = s[r]
            table[ord(char) - ord('A')] += 1
            win_size = r - l + 1
            max_table = max(table)
            if win_size - max_table <= k:
                # Valid window
                res = max(res, win_size)
            else:
                # Invalid window
                char = s[l]
                table[ord(char) - ord('A')] -= 1
                l += 1
            r += 1
        return res



# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         table = [0]*26
#         currMaxCnt = 0
#         maxLen = 0
#         l = 0
#         for r in range(len(s)):
#             table[ord(s[r])-ord('A')] += 1
#             currMaxCnt = max(currMaxCnt, table[ord(s[r])-ord('A')])
#             while r-l+1-currMaxCnt>k:
#                 table[ord(s[l])-ord('A')]-= 1
#                 l += 1
#             maxLen = max(maxLen, r-l+1)
#         return maxLen                