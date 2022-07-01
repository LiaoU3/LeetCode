# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                slow2 = head
                if slow == slow2:
                    return slow
                while slow!=slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        return None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        while head:
            if head in seen:
                return head
            seen.append(head)
            head = head.next