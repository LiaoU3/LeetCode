# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def dfs(node):
            if self.res:
                return
            if not node:
                return
            if node.val == subRoot.val:
                if compare(node, subRoot):
                    self.res = True
            dfs(node.left)
            dfs(node.right)
        
        def compare(node1, node2):
            if not node1 and not node2:  # If they are both None
                return True
            if not node1 or not node2:  # If one of them is None
                return False
            if node1.val != node2.val:
                return False
            if compare(node1.left, node2.left) and compare(node1.right, node2.right):
                return True
            return False
        
        dfs(root)
        return self.res