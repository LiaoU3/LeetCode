# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# cleaner solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left, right):
            if left > right:
                return None
            middle = (left+right) // 2
            father = TreeNode(nums[middle])
            father.left  = build(left, middle-1)
            father.right = build(middle+1, right)
            return father
        return build(0, len(nums)-1)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def toBST(node, nums_left, nums_right):
            if len(nums_left)  == 0:
                return
            node.left  = TreeNode(nums_left[len(nums_left)//2])
            toBST(node.left, nums_left[:len(nums_left)//2], nums_left[len(nums_left)//2+1:])
            if len(nums_right) == 0:
                return
            node.right = TreeNode(nums_right[len(nums_right)//2])
            toBST(node.right, nums_right[:len(nums_right)//2], nums_right[len(nums_right)//2+1:])
        ans = TreeNode(nums[len(nums)//2])
        toBST(ans, nums[:len(nums)//2], nums[len(nums)//2+1:])

        return ans
        