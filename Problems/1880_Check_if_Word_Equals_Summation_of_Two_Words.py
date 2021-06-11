# a fancy way to do this LOL
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        numberize = lambda s : int(''.join(str(ord(c) - 97) for c in s))
        return numberize(firstWord) + numberize(secondWord) == numberize(targetWord)

# class Solution:
#     def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
#         num1 = ''
#         for c in firstWord:
#             num1 += str(ord(c) - 97)
#         num1 = int(num1)

#         num2 = ''
#         for c in secondWord:
#             num2 += str(ord(c) - 97)
#         num2 = int(num2)

#         num3 = ''
#         for c in targetWord:
#             num3 += str(ord(c) - 97)
#         num3 = int(num3)
#         return num1 + num2 == num3
solution = Solution()
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(solution.isSumEqual(firstWord, secondWord, targetWord))