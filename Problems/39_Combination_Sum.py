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