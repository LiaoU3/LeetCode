# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        def traverse(node, seenBig):
            if not node:
                return
            if node.val >= seenBig:
                nonlocal cnt
                cnt += 1
            seenBig = max(seenBig, node.val)
            traverse(node.left, seenBig)
            traverse(node.right, seenBig)
        
        traverse(root, -10**4-1)
        return cnt