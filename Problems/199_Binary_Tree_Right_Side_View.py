from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(node: TreeNode, height: int):
            if node is None:
                return
            if height == len(res):
                res.append(node.val)
            traverse(node.right, height+1)
            traverse(node.left, height+1)
        traverse(root, 0)
        return res

# bfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        qu = deque([root])
        res = []
        while qu:
            length = len(qu)
            res.append(qu[length-1].val)
            for i in range(length):
                node = qu.popleft()
                if node.left is not None:
                    qu.append(node.left)
                if node.right is not None:
                    qu.append(node.right)
        return res