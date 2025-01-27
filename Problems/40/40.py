class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            if i == len(candidates):
                return

            curr.append(candidates[i])
            backtrack(i + 1, total + candidates[i], curr)
            curr.pop()

            for j in range(i + 1, len(candidates)):
                if candidates[i] != candidates[j]:
                    backtrack(j, total, curr)
                    return

        backtrack(0, 0, [])
        return res