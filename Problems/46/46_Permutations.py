from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(curr: List[int]):
            if len(curr) == len(nums):
                res.append(curr)
                return
            for num in nums:
                if num in curr:
                    continue
                helper(curr + [num])
        helper([])
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(currNums, usedIndex):
            if  len(currNums) == len(nums):
                res.append(currNums)
                return
            for i, num in enumerate(nums):
                if i in usedIndex:
                    continue
                helper(currNums + [num], usedIndex + [i])
        
        helper([], [])
        return res
                

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(curr_list, history_index_list):
            if len(curr_list)==len(nums):
                res.append(curr_list)
                return 
            for i in range(len(nums)):
                if i in history_index_list:
                    continue
                helper(curr_list+[nums[i]], history_index_list+[i])
        helper([], [])
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))