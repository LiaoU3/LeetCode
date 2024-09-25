from typing import Optional, List
# Definition for a binary tree node.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None
        num = preorder[0]
        node = TreeNode(num)
        idx = inorder.index(num)
        node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if len(preorder) == 0: return None
#         if len(preorder) == 1: return TreeNode(preorder[0])
#         i = inorder.index(preorder[0])
#         return TreeNode(val = preorder[0], 
#                         left = self.buildTree(preorder[1:i+1], inorder[:i]), 
#                         right = self.buildTree(preorder[i+1:], inorder[i+1:]))