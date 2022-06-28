from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def helper(curr_str: str, curr_index: int):
            if len(curr_str)==len(s):
                res.append(curr_str)
                return
            curr_index += 1               
            if s[curr_index].isalpha():
                helper(curr_str+s[curr_index].lower(), curr_index)
                helper(curr_str+s[curr_index].upper(), curr_index)
            else:
                helper(curr_str + s[curr_index], curr_index)
        helper("", -1)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "a1b2"
    print(sol.letterCasePermutation(s))