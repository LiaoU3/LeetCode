# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def binary_search(l, r):
            m = (l + r) // 2
            ret = guess(m)
            if ret == 0:
                return m
            elif ret == -1:
                return binary_search(l, m - 1)
            else:
                return binary_search(m + 1, r)

        return binary_search(1, n)
