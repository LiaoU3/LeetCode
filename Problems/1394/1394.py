class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = 0
        counter = Counter(arr)
        for num, freq in counter.items():
            if num == freq:
                res = max(res, num)
        return res if res else -1
