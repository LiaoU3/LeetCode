class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num):
            if num > n:
                return
            res.append(num)
            dfs(num * 10)
            if num % 10 != 9:
                dfs(num + 1)

        dfs(1)
        return res
