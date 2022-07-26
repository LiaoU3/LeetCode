# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node):
            if not node:
                return 
            if node == p or node == q:
                return node
            l = traverse(node.left)
            r = traverse(node.right)
            if l and r:
                return node
            return l or r
        return traverse(root)