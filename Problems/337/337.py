# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            """Return num1, num2
            num1: the max value if include the node itself
            num2: the max value not include the node itself
            """
            if node is None:
                return 0, 0
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            return node.val + l2 + r2, max(l1, l2) + max(r1, r2)

        return max(dfs(root))
