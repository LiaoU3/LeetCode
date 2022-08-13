# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def traverse(node):
            if not node:
                return 0
            l = traverse(node.left)
            r = traverse(node.right)
            self.longest = max(self.longest, l + r)
            return max(l, r) + 1
        traverse(root)
        return self.longest

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def traverse(node):
            nonlocal longest
            if not node:
                return 0
            l = traverse(node.left)
            r = traverse(node.right)
            longest = max(longest, l + r)
            return max(l, r) + 1
        traverse(root)
        return longest