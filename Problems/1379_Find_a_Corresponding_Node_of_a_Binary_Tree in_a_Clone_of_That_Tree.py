from Operation_of_ListNode import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(original, cloned):
            if original == target:
                return cloned
            if original.left:
                node = traverse(original.left, cloned.left)
                if node:
                    return node
            if original.right:
                node = traverse(original.right, cloned.right)
                if node:
                    return node

        return traverse(original, cloned)

# def main():
#     null = None
#     tree = [7,4,3,null,null,6,19]
#     target = 3
#     tree = List2Node(tree)

#     solution = Solution()
#     print(solution.getTargetCopy(tree, tree.copy(), target))