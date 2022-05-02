class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left  = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums

def main():
    solution = Solution()
    nums = [0, 1, 2, 3, 4, 5]
    print(solution.sortArrayByParity(nums))

if __name__ == '__main__':
    main()