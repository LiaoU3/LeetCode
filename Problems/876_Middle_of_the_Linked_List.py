# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        middle_node = head
        cnt = -1
        while curr_node:
            curr_node  = curr_node.next
            if cnt %2 == 0:
                middle_node = middle_node.next
            cnt += 1
        return middle_node