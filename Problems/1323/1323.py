class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = list(str(num))
        for i, n in enumerate(nums):
            if n == "6":
                nums[i] = "9"
                break
        return int("".join(nums))
