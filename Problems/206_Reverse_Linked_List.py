from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# clear Colution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre  = None
        curr = head
        # reverse curr and pre
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return None
#         pre  = None
#         curr = head
#         nxt  = head.next

#         # reverse curr and pre
#         while curr:
#             curr.next = pre
#             pre = curr
#             curr = nxt
#             if nxt:
#                 nxt = nxt.next
#         return pre