# Definition for a binary tree node.
from typing_extensions import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.k = None
        self.ans = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node or self.k<0:
            return
        self.traverse(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return 
        self.traverse(node.right)

