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