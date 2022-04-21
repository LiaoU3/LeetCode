class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= 2:
            return s
        ans = ""
        for i in range(0, len(s), 2*numRows-2):
            ans += s[i]

        for i in range(1, numRows-1):
            for j in range(i, len(s), 2*numRows-2):
                ans += s[j]
                if j + (2*numRows-2) - 2*i <len(s):
                    ans += s[j + (2*numRows-2) - 2*i]
        
        for i in range(numRows-1, len(s), 2*numRows-2):
            ans += s[i]
        
        return ans

def main():
    solution = Solution()
    input = "ABC"
    row = 1
    print(solution.convert(input, row))

if __name__ == '__main__':
    main()