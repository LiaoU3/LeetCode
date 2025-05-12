class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        def is_legal(i, even):
            if even:
                if i % 2 == 0:
                    if arr[i] >= arr[i + 1]:
                        return False
                else:
                    if arr[i] <= arr[i + 1]:
                        return False
            else:
                if i % 2 == 0:
                    if arr[i] <= arr[i + 1]:
                        return False
                else:
                    if arr[i] >= arr[i + 1]:
                        return False
            return True

        l = 0
        for r in range(len(arr) - 1):
            if not is_legal(r, True):
                l = r + 1
            res = max(res, r - l + 2)

        l = 0
        for r in range(len(arr) - 1):
            if not is_legal(r, False):
                l = r + 1
            res = max(res, r - l + 2)

        return res