class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        count = 0
        max_val = 0
        for i, value in enumerate(flips):
            max_val = max(max_val, value)
            if max_val == i+1:
                count += 1
        return count

def main():
    solution = Solution()
    flips = [5,2,4,1,3]
    ans = solution.numTimesAllBlue(flips)
    print(ans)

if __name__ == '__main__':
    main()