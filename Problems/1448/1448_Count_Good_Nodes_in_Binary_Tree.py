# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_parent):
            if node is None:
                return 0
            cnt = 0
            if node.val >= max_parent:
                cnt += 1
            max_parent = max(max_parent, node.val)
            cnt += dfs(node.left, max_parent)
            cnt += dfs(node.right, max_parent)
            return cnt
        return dfs(root, root.val)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(node, curr_max):
            if node is None:
                return
            if node.val >= curr_max:
                self.res += 1
            curr_max = max(curr_max, node.val)
            traverse(node.left, curr_max)
            traverse(node.right, curr_max)
        traverse(root, root.val)
        return self.res

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         cnt = 0
        
#         def traverse(node, seenBig):
#             if not node:
#                 return
#             if node.val >= seenBig:
#                 nonlocal cnt
#                 cnt += 1
#             seenBig = max(seenBig, node.val)
#             traverse(node.left, seenBig)
#             traverse(node.right, seenBig)
        
#         traverse(root, -10**4-1)
#         return cnt