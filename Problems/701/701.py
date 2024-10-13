# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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