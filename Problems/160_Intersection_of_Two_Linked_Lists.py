from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pointA = headA
        pointB = headB

        while pointA or pointB:
            if pointA == pointB:
                return pointA
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return None