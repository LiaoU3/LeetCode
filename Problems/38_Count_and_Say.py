class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for _ in range(n-1):
            curr_num = ans[0]
            count_num = 1
            ans_next = ""
            for num in ans[1:]:
                if num == curr_num:
                    count_num += 1
                else:
                    ans_next = ans_next + str(count_num) + curr_num
                    curr_num = num
                    count_num = 1
            ans = ans_next + str(count_num) + curr_num
        return ans

if __name__ == '__main__':
    sol = Solution()
    n = 1
    print(sol.countAndSay(n))