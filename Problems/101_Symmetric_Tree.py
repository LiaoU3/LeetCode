from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Best and cleanest solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return traverse(node1.left, node2.right) and traverse(node1.right, node2.left)
        return traverse(root, root)


class Solution:
    def __init__(self):
        self.flag = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not self.flag:
                return
            if not node1 and not node2:
                return
            if (node1 and not node2) or (not node1 and node2) or node1.val != node2.val:
                self.flag = False
                return
            traverse(node1.left, node2.right)
            traverse(node1.right, node2.left)
        traverse(root, root)
        return self.flag

# another solution using yield
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def traverse(node1, node2):
#             if not node1 and not node2:
#                 return 
#             if (node1 and not node2) or (not node1 and node2) or node1.val != node2.val:
#                 yield False
#             yield from traverse(node1.left, node2.right)
#             yield from traverse(node1.right, node2.left)

#         trav = traverse(root, root)
#         while True:
#             ret = next(trav, 'end')
#             if ret == False:
#                 return False
#             if ret == 'end':
#                 break
#         return True