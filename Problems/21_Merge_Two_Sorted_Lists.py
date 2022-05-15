from Operation_of_ListNode import *
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        # print(ListNodetoList(ans))
        curr = ans
        while l1 or l2:
            num1 = l1.val if l1 else 101
            num2 = l2.val if l2 else 101
            curr.next = ListNode()
            if num1 < num2:
                curr.next.val = num1
                l1 = l1.next if l1 else l1
            else:
                curr.next.val = num2
                l2 = l2.next if l2 else l2
            curr = curr.next
            # print(ListNodetoList(ans.next))
        return ans.next


l1 = []
l2 = [1, 3, 4]
l1 = List2Node(l1)
l2 = List2Node(l2)

print(Node2List(l1))

solution = Solution()
ln = solution.mergeTwoLists(l1, l2)
# print(ListNodetoList(ln))