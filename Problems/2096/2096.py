# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        start_seq = []
        dest_seq = []
        def dfs(node):
            if node is None:
                return 0
            curr = 0
            if node.val == startValue:
                curr = 1
            elif node.val == destValue:
                curr = 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 1 or right == 1:
                start_seq.append("U")
            if left == 2:
                dest_seq.append("L")
            if right == 2:
                dest_seq.append("R")
            return curr + left + right

        dfs(root)

        return "".join(start_seq + dest_seq[::-1])