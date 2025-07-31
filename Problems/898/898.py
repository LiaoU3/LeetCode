class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = set()
        for num in arr:
            nxt = {num | num2 for num2 in curr}
            nxt.add(num)
            res |= nxt
            curr = nxt
        return len(res)
