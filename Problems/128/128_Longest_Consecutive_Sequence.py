# Union Find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        parent = {}  # key: num, val: parent of the num
        rank = {}  # key: num, val: rank of the num

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return True
            r1 = rank[p1]
            r2 = rank[p2]
            if r2 > r1:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            parent[p2] = p1
            return False
        
        for num in nums:
            if num in rank:
                continue
            rank[num] = 1
            parent[num] = num
            if num - 1 in rank:
                union(num, num - 1)
            if num + 1 in rank:
                union(num, num + 1)

        return max(rank.values())

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
