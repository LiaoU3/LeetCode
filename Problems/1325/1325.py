# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if node is None:
            return None
        node.left = self.removeLeafNodes(node.left, target)
        node.right  = self.removeLeafNodes(node.right, target)
        if node.left is None and node.right is None and node.val == target:
            return None
        return node


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right  = dfs(node.right)
            if node.left is None and node.right is None and node.val == target:
                return None
            return node

        return dfs(root)