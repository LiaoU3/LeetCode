# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)
        def dfs(node, order, level):
            if not node:
                return
            hm[order].append((level, node.val))
            dfs(node.left,  order - 1, level + 1)
            dfs(node.right, order + 1, level + 1)
        dfs(root, 0, 0)
        res = []
        for i in sorted(hm.keys()):
            tmp = []
            for j in sorted(hm[i]):
                tmp.append(j[1])
            res.append(tmp)
        return res