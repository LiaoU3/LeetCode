class Solution:
    def fib(self, n: int) -> int:
        pre = 1
        prepre = 0
        if n==prepre:
            return 0
        if n==pre:
            return 1
        cnt = 1
        for _ in range(n-1):
            curr = pre+prepre
            # print(curr, pre, prepre)
            prepre = pre
            pre = curr
        return curr