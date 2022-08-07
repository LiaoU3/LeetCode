# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        oddTail = head
        evenHead = head.next
        evenTail = head.next
        
        curr = head.next.next
        isOdd = True
        while curr:
            if isOdd:
                evenTail.next = curr.next
                evenTail = evenTail.next
                oddTail.next = curr
                oddTail = oddTail.next
            curr = curr.next
            isOdd = not isOdd
        
        oddTail.next = evenHead
        
        return head