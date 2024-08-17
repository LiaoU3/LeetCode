# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        # Find the middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow_prev = slow
            slow = slow.next
        slow_prev.next = None
        node2 = slow
        # Reverse the link list 2
        prev = None
        curr = node2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge two link list
        curr1 = head
        curr2 = prev
        while curr1.next:
            curr1_next = curr1.next
            curr2_next = curr2.next
            curr1.next = curr2
            curr2.next = curr1_next
            curr1 = curr1_next
            curr2 = curr2_next
        curr1.next = curr2
