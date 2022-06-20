from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # great common divisor
        def gcd(m, n):
            if n == 0:
                return m 
            else:
                return gcd(n, m % n)

        # make k in range(0, length)
        length = len(nums)
        k %=length

        # if k == 0 whick means no rotate, then break out
        if not k:
            return

        # get the loop count i.e. length = 6, k = 4 -> count = 2 = gcd(6, 4) ->(0, 4, 2, 0), (1, 5, 3, 1)
        count = gcd(length, k)

        for i in range(count):
            pre_num = nums[i]
            curr_point = i+k
            while curr_point!=i:
                pre_num, nums[curr_point] = nums[curr_point], pre_num
                curr_point += k
                curr_point %= length
            nums[i] = pre_num

if __name__ =='__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6]
    k = 4
    # k = 1
    sol.rotate(nums, k)
    print(nums)