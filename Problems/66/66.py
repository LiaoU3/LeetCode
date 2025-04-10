class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                break
            digits[i] = 0
        if digits[0] == 0:
            digits = [1] + digits
        return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1] + [0]
        digits[0] += 1

        for i in range(len(digits) - 1):
            if digits[i] == 10:
                digits[i + 1] += 1
                digits[i] = 0
            else:
                break
        
        digits = digits[::-1]
        if digits[0] == 0:
            digits = digits[1:]
        return digits