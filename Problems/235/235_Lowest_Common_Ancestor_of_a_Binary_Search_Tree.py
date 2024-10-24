# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val>p.val and node.val>q.val:
                node = node.left
            elif node.val<p.val and node.val<q.val:
                node = node.right
            else:
                return node

# recursion solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.rught, p, q)
        else:
            return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(node):
            if p.val >= node.val >= q.val or p.val <= node.val <= q.val:
                return node
            elif p.val > node.val and q.val > node.val:
                return traverse(node.right)
            else:
                return traverse(node.left)
        return traverse(root)