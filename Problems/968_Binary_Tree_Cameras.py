from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.camera_count = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        # None: 0, Covered: 1, Camera: 2
        def traverse(node):
            if not node:
                return 1
            l = traverse(node.left)
            r = traverse(node.right)
            if l == 0 or r == 0:
                self.camera_count += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0
        
        if traverse(root):
            return self.camera_count
        else:
            return self.camera_count+1