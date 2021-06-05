class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ret = ""
        index = 0
        max_index = min(len(x) for x in strs)
        break_away = False
        while index < max_index:
            curr_c = strs[0][index]
            for str_ in strs:
                if str_[index] != curr_c:
                    break_away = True
                    break
            else:
                ret += curr_c
            if break_away:
                break
            index += 1
        return ret

solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))