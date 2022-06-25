from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        pre_pre = pre = curr = float('-Inf')
        for num in nums:
            pre_pre = pre
            pre = curr
            curr = num
            if pre > curr:
                count += 1
                if count == 2:
                    return False
                if pre_pre>curr:
                    curr = pre
        return True
if __name__ == '__main__':
    sol = Solution()
    nums = [3,4,2,3]
    print(sol.checkPossibility(nums))