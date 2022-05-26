# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from Operation_of_ListNode import *

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        point = head
        while curr:
            curr = curr.next
            if n!=-1:
                n -= 1
            else:
                point = point.next
        if n == -1:
            point.next = point.next.next
            return head
        else:
            return point.next

def main():
    sol = Solution()
    head = List2Node([1,2])
    n = 1
    print(Node2List(sol.removeNthFromEnd(head, n)))
if __name__ == '__main__':
    main()