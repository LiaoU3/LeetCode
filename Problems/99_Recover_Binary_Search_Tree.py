# Definition for a binary tree node.
from inspect import stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# traverse all element in BST by inorder traversal, then sort the value
# Note : It's not the fastest solution to this problem, but it's definitely a simplist one
class Solution:
    def __init__(self):
        self.stack = []

    def recoverTree(self, root: TreeNode) -> None:
        curr = root
        self.traverse(curr)
        sorted_vals = sorted(n.val for n in self.stack)
        for i in range(len(sorted_vals)):
            self.stack[i].val = sorted_vals[i]

    def traverse(self, curr):
        if not curr:
            return
        self.traverse(curr.left)
        self.stack.append(curr)
        self.traverse(curr.right)