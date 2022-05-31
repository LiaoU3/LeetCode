class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1
        prepre = 1
        if n == 1:
            return 1
        for _ in range(2, n+1):
            curr = pre + prepre
            prepre = pre
            pre = curr
        return curr