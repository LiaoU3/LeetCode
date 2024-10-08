# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from Operation_of_ListNode import *

# Best clean solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        front = back = dummy
        for _ in range(n):
            front = front.next
        while front.next:
            front = front.next
            back = back.next
        back.next = back.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        cnt = 0
        while fast.next:
            fast = fast.next
            if cnt == n:
                slow = slow.next
            else:
                cnt += 1
        slow.next = slow.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        slow_pre = head
        while fast:
            if n<=0:
                slow_pre = slow
                slow = slow.next
            fast = fast.next
            n -= 1
        slow_pre.next = slow.next
        # Slow is about to move
        if n==0:
            return head.next
        # Didn't even move
        if slow==slow_pre:
            return None
        # regular case
        return head

def main():
    sol = Solution()
    head = List2Node([1,2])
    n = 1
    print(Node2List(sol.removeNthFromEnd(head, n)))
if __name__ == '__main__':
    main()