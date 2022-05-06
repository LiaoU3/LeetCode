class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        index = 1
        # stack = [c, count]
        stack = [[s[0], 1]]

        while index < len(s):
            if stack and stack[-1][0] == s[index]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[index], 1])
            index += 1
        result = ""
        for c, times in stack:
            result += c*times
        return result

# TLE 
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         while True:
#             i = 0
#             is_final =  True
#             while i+k <= len(s):
#                 if len(set(s[i:i+k])) == 1:
#                     is_final = False
#                     if i+k < len(s):
#                         s = s[:i] + s[i+k:]
#                     else:
#                         s = s[:i]
#                 else:
#                     i += 1
#             if is_final:
#                 break
#         return s

def main():
    s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
    k = 4
    solution = Solution()
    print(solution.removeDuplicates(s,k))

if __name__ == '__main__':
    main()