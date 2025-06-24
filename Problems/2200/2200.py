class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0
        for i, num in enumerate(nums):
            if num == key:
                l = max(r, i - k)
                r = min(len(nums) - 1, i + k) + 1
                for j in range(l, r):
                    res.append(j)
        return res


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idxes = []
        for i, num in enumerate(nums):
            if num == key:
                key_idxes.append(i)
        res = []
        j = 0
        for i in range(len(nums)):
            while j < len(key_idxes) and i > key_idxes[j] + k:
                j += 1
            if j == len(key_idxes):
                break
            if key_idxes[j] - k <= i <= key_idxes[j] + k:
                res.append(i)
        return res
