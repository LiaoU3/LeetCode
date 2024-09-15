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

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         num1 = 0
#         digit = 0
#         while l1:
#             num1 += l1.val * 10 ** digit
#             digit += 1
#             l1 = l1.next
#         num2 = 0
#         digit = 0
#         while l2:
#             num1 += l2.val * 10 ** digit
#             digit += 1
#             l2 = l2.next
#         total = num1 + num2
#         dummy = curr = ListNode()
#         num = total % 10
#         total //= 10
#         node = ListNode(num)
#         curr.next = node
#         curr = curr.next
#         while total:
#             num = total % 10
#             total //= 10
#             node = ListNode(num)
#             curr.next = node
#             curr = curr.next
#         return dummy.next