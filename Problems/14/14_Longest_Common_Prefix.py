# cleanest solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(len(res)):
            for string in strs[1:]:
                if i == len(string) or strs[0][i] != string[i]:
                    return res[:i]
        return res

# cleaner solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i == len(string) or strs[0][i] != string[i]:
                    return res
            res += strs[0][i]
        return res

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        ret = ""
        index = 0
        max_index = min(len(x) for x in strs)
        break_away = False
        while index < max_index:
            curr_c = strs[0][index]
            for str_ in strs[1:]:
                if str_[index] != curr_c:
                    break_away = True
                    break
            else:
                ret += curr_c
            if break_away:
                break
            index += 1
        return ret

# solution = Solution()
# print(solution.longestCommonPrefix(["dog","racecar","car"]))