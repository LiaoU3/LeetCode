# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        res = 0
        nums = nums[::-1]
        for i, num in enumerate(nums):
            res += nums[i] * 2 ** i

        return res
