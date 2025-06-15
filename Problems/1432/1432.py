class Solution:
    def maxDiff(self, num: int) -> int:
        num_ls = []
        while num:
            num_ls.append(num % 10)
            num //= 10

        for i in range(len(num_ls) - 1, -1, -1):
            to_replace = num_ls[i]
            if num_ls[i] != 9:
                break

        max_num = 0
        for i in range(len(num_ls)):
            digit = num_ls[i] if num_ls[i] != to_replace else 9
            max_num += digit * 10 ** i

        to_replace = num_ls[-1]
        if to_replace == 1:
            for i in range(len(num_ls) - 1, -1, -1):
                to_replace = num_ls[i]
                if num_ls[i] not in (0, 1):
                    break

        min_num = 0
        replaced = 1 if to_replace == num_ls[-1] else 0
        for i in range(len(num_ls)):
            digit = num_ls[i] if num_ls[i] != to_replace else replaced
            min_num += digit * 10 ** i

        return max_num - min_num


num = 123456
sol = Solution()
print(sol.maxDiff(num))
