# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = self.inorder(root)
        self.next_num = next(self.iterator, None)

    def next(self) -> int:
        curr = self.next_num
        self.next_num = next(self.iterator, None)
        return curr
        
    def hasNext(self) -> bool:
        return self.next_num is not None
    
    def inorder(self, node):
        if not node:
            return
        yield from self.inorder(node.left)
        yield node.val
        yield from self.inorder(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()