# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
    
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            traverse(node.right)
            if node.left:
                nxt = node.left
                while nxt.right:
                    nxt = nxt.right
                nxt.right = node.right
                node.right = node.left
            node.left = None

        traverse(root)