# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# c;ean solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        stack.append(curr)
        
        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            
# class Solution:
#     def __init__(self):
#         self.k = None
#         self.ans = None

#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         self.k = k
#         self.traverse(root)
#         return self.ans

#     def traverse(self, node):
#         if not node or self.k<0:
#             return
#         self.traverse(node.left)
#         self.k -= 1
#         if self.k == 0:
#             self.ans = node.val
#             return 
#         self.traverse(node.right)