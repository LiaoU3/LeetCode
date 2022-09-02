# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        qu = deque([root])
        
        while qu:
            length = len(qu)
            total = 0
            for _ in range(length):
                node = qu.popleft()
                total += node.val
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(total / length)
        return res