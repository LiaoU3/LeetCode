class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num_set = set()
        num = ''
        for c in word:
            if c.isnumeric():
                num += c
            elif len(num) != 0:
                    num_set.add(int(num))
                    num = ''
        return len(num_set)

solution = Solution()
word = "leet1234code234"

print(solution.numDifferentIntegers(word))