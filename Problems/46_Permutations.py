from typing import List

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