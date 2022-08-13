from collections import defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use dict makes it faster
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        hm = defaultdict(int)
        hm[0] += 1
        def traverse(node, currSum):
            nonlocal cnt
            if not node:
                return
            currSum += node.val
            cnt += hm[currSum - targetSum]
            hm[currSum] += 1
            traverse(node.left, currSum)
            traverse(node.right, currSum)
            hm[currSum] -= 1
        traverse(root , 0)
        return cnt

# use nonlocal
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def traverse(node, seen : List[int]):
            nonlocal cnt
            if not node:
                return
            for num in seen:
                if node.val + seen[-1] - num == targetSum:
                    cnt += 1
            traverse(node.left, seen + [node.val + seen[-1]])
            traverse(node.right, seen + [node.val + seen[-1]])               
        traverse(root , [0])
        return cnt

# use self
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0
        def traverse(node, seen : List[int]):
            if not node:
                return
            for num in seen:
                if node.val + seen[-1] - num == targetSum:
                    self.cnt += 1
            traverse(node.left, seen + [node.val + seen[-1]])
            traverse(node.right, seen + [node.val + seen[-1]])               
        traverse(root , [0])
        return self.cnt