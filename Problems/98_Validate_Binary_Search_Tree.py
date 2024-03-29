from typing import Optional
from Operation_of_ListNode import List2Node
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# cleanset solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lowerBound = float('-inf'), upperBound = float('inf')) -> bool:
        if not root:
            return True
        if not(upperBound > root.val > lowerBound):
            return False
        return  self.isValidBST(root.left, lowerBound, root.val) and self.isValidBST(root.right, root.val, upperBound)

# cleaner solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, lowerBound, upperBound):
            if not node:
                return True
            if not(upperBound > node.val > lowerBound):
                return False
            return  traverse(node.left, lowerBound, node.val) and traverse(node.right, node.val, upperBound)
        
        return traverse(root, float('-inf'), float('inf'))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(node: TreeNode, minVal, maxVal):
            if node is None:
                return True
            if minVal<node.val<maxVal:
                return traverse(node.left, minVal, node.val) and traverse(node.right, node.val, maxVal)
            else:
                return False
        return traverse(root, float('-inf'), float('inf'))


# Wrong Solution without considering the parents' value
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         qu = deque([root])
#         while qu:
#             length = len(qu)
#             for _ in range(length):
#                 curr = qu.popleft()                    
#                 if curr.left is not None:
#                     if curr.left.val >= curr.val:
#                         return False
#                     qu.append(curr.left)
#                 if curr.right is not None:
#                     if curr.right.val <= curr.val:
#                         return False
#                     qu.append(curr.right)
#         return True
