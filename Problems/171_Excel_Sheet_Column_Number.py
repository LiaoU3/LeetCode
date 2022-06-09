class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = 0
        total = 0
        for c in columnTitle[::-1]:
            total += (ord(c) - 64)* 26**power
            power += 1
        return total