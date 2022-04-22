# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        start = head.next
        pre = None
        while curr and curr.next:
            nxt = curr.next
            if pre:
                pre.next = nxt
            temp = nxt.next
            nxt.next = curr
            curr.next = temp
            pre = curr
            curr = curr.next

        return start or head