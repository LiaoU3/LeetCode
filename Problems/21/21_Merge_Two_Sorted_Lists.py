from Operation_of_ListNode import *
from typing import Optional


# Recurrsion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            res = list1
            res.next = self.mergeTwoLists(list1.next, list2)
        else:
            res = list2
            res.next = self.mergeTwoLists(list1, list2.next)

        return res


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while list1 or list2:
            v1 = list1.val if list1 else float("Inf")
            v2 = list2.val if list2 else float("Inf")
            if v1 < v2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dummy.next


# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         res = ListNode()
#         curr = res
#         while l1 and l2:
#             if l1.val<l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
        
#         if l1:
#             curr.next = l1
#         elif l2:
#             curr.next = l2
#         return res.next

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         ans = ListNode()
#         # print(ListNodetoList(ans))
#         curr = ans
#         while l1 or l2:
#             num1 = l1.val if l1 else 101
#             num2 = l2.val if l2 else 101
#             curr.next = ListNode()
#             if num1 < num2:
#                 curr.next.val = num1
#                 l1 = l1.next if l1 else l1
#             else:
#                 curr.next.val = num2
#                 l2 = l2.next if l2 else l2
#             curr = curr.next
#             # print(ListNodetoList(ans.next))
#         return ans.next

if __name__ == '__main__':
    l1 = []
    l2 = [1, 3, 4]
    l1 = List2Node(l1)
    l2 = List2Node(l2)

    print(Node2List(l1))

    solution = Solution()
    ln = solution.mergeTwoLists(l1, l2)
    # print(ListNodetoList(ln))