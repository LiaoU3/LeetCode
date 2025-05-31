class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(i, total, curr):
            if total > target:
                return
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates):
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(j + 1, total + candidates[j], curr)
                curr.pop()

        backtrack(0, 0, [])
        return res


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