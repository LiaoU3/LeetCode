# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("Inf")

        def dfs(node):
            if node == None:
                return 0
            r = dfs(node.right)
            l = dfs(node.left)
            self.res = max(self.res, node.val + r + l, node.val + r, node.val + l, node.val)
            return max(node.val + r, node.val + l, node.val)
        dfs(root)
        return self.res