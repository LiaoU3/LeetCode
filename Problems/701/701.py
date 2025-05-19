# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(val=float("Inf"), left=root)

        def dfs(node):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    dfs(node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right)

        dfs(dummy)    
        return dummy.left


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(float("Inf"))
        dummy.left = root
        pre = None
        curr = dummy
        while curr:
            pre = curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        if pre.val > val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return dummy.left