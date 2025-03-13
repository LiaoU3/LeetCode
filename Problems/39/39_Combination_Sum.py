class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(curr, total, i):
            if total == target:
                res.append(curr.copy())
                return
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(curr, total + candidates[j], j)
                curr.pop()

        backtrack([], 0, 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            for j, num in enumerate(candidates):
                if j < i:
                    continue
                curr.append(num)
                backtrack(curr, j, total + num)
                curr.pop()
        backtrack([], 0, 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(curr, currSum, index):
            for i in range(index, len(candidates)):
                cand = candidates[i]
                if currSum + cand > target:
                    return
                elif currSum + cand == target:
                    res.append(curr+[cand])
                else:
                    helper(curr + [cand], currSum + cand, i)
        
        helper([], 0, 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        
        def traverse(cands, curr):
            if sum(cands) == target:
                res.append(cands)
                return
            if sum(cands) > target:
                return
            for i in range(curr, n):
                traverse(cands + [candidates[i]], i)
        traverse([], 0)
        return res