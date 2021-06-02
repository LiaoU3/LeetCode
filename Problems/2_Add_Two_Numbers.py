# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        curr = ans
        carry = 0
        while l1 or l2 :
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry
            carry = sum //10
            curr.next = ListNode(sum%10)
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            curr.next = ListNode(1)
        return ans.next