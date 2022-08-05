class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        
        nums = [0]*(len1 + len2)
        topDigit = 0
        for i in range(len1):
            for j in range(len2):
                nums[i + j] += int(num1[len1 - 1 - i]) * int(num2[len2 - 1 - j])
                if nums[i + j]:
                    topDigit = max(topDigit, i + j)
        res = ""
        for i in range(topDigit+1):
            res = str(nums[i] % 10) + res
            nums[i+1] += nums[i] // 10
        if nums[topDigit+1] > 0:
            res = str(nums[topDigit+1]) + res
        return res

if __name__ == '__main__':
    sol = Solution()
    num1 = "123"
    num2 = "456"
    print(sol.multiply(num1, num2))