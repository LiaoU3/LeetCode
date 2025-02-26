class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return
            backtrack(curr, i + 1)
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
        
        backtrack([], 0)

        return res
