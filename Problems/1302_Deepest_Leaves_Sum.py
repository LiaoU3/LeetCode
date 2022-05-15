from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        curr_row = [root]
        while curr_row:
            next_row = []
            for node in curr_row:
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            if not next_row:
                return sum([node.val for node in curr_row])
            curr_row = next_row