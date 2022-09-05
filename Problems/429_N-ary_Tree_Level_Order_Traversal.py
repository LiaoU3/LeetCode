"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        qu = deque([root])
        while qu:
            length = len(qu)
            tmp = []
            for _ in range(length):
                curr = qu.popleft()
                tmp.append(curr.val)
                for child in curr.children:
                    qu.append(child)
            res.append(tmp)
        return res