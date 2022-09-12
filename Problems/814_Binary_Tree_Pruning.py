# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            if not node:
                return True
            l = traverse(node.left)
            if l:
                node.left = None
            r = traverse(node.right)
            if r:
                node.right = None
            return not node.val and l and r
        return root if not traverse(root) else None