# Union Find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parent = {}  # num: root
        rank = {}  # num: length
        res = 1

        def find(num):
            """find the root and update the root for all nodes in the path"""
            if num == parent[num]:  # found root
                return num
            parent[num] = find(parent[num])  # update the root
            return parent[num]

        def union(num1, num2):
            """merge num1 and num2""" 
            root1 = find(num1)
            root2 = find(num2)
            if root1 == root2:
                return
            if num1 < num2:
                small = num1
                root_small = root1
                big = num2
                root_big = root2
            else:
                small = num2
                root_small = root2
                big = num1
                root_big = root1
            parent[big] = root_small
            rank[root_small] += rank[root_big]
            return rank[root_small]
        
        for num in nums:
            if num in parent:
                continue
            parent[num] = num
            rank[num] = 1
            if num + 1 in parent:
                res = max(res, union(num, num + 1))
            if num - 1 in parent:
                res = max(res, union(num - 1, num))
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            length = 1
            while num + 1 in num_set:
                num += 1
                length += 1
            res = max(res, length)
        return res
