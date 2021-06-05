class Solution:
    def romanToInt(self, s: str) -> int:
        val_ls = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        sum = 0
        prev_val = float('inf')
        for c in s:        
            sum += val_ls[c]
            if prev_val < val_ls[c]:
                sum -= 2 * prev_val
            prev_val = val_ls[c]
        return sum

# solution = Solution()
# print(solution.romanToInt('MCMXCIV'))