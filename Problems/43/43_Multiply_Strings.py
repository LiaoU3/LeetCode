class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        nums = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                multiplied = (ord(n1) - ord("0")) * (ord(n2) - ord("0"))
                nums[i + j] += multiplied % 10
                nums[i + j + 1] += multiplied // 10

        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i] // 10
            nums[i] %= 10

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                break

        res = ""
        for j in range(i, -1, -1):
            res += str(nums[j])
        
        return res

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