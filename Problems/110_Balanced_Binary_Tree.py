# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity : O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def traverse(node : Optional[TreeNode]) -> int:
            if not self.balanced:
                return 0
            if not node:
                return 1
            l = traverse(node.left)
            r = traverse(node.right)
            if abs(l-r) > 1:
                self.balanced = False
                return 0
            return max(l, r) + 1
        traverse(root)
        return self.balanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(node : Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            return max(l, r) + 1
        
        def traverse(node):
            if not node:
                return True
            l = depth(node.left)
            r = depth(node.right)
            if abs(l-r) > 1:
                return False
            return traverse(node.left) and traverse(node.right)
        return traverse(root)