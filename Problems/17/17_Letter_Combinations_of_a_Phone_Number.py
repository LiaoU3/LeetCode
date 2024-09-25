class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            }
        res = []
        def backtrack(string):
            if len(string) == len(digits):
                res.append(string)
                return
            i = len(string)
            digit = digits[i]
            for c in hash_table[digit]:
                backtrack(string + c)
        backtrack("")
        return res if digits else []

# class Solution:
#     def letterCombinations(self, digits: str) -> list:
#         buttons = {
#             '2':'abc',
#             '3':'def',
#             '4':'ghi',
#             '5':'jkl',
#             '6':'mno',
#             '7':'pqrs',
#             '8':'tuv',
#             '9':'wxyz'
#         }
#         if len(digits) == 0:
#             return []
#         elif len(digits) == 1:
#             return list(buttons[digits[0]])
#         else:
#             prev = self.letterCombinations(digits[:-1])
#             last = buttons[digits[-1]]
#             return [s + c for s in prev for c in last]

# solution = Solution()
# digits = '234'
# print(solution.letterCombinations(digits))
