import sys
sys.path.append('/home/u3/Desktop/LeetCode')
from Operation_of_ListNode import *
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        curr = ans
        while l1 or l2:
            num1 = l1.val
            num2 = l2.val
            curr.next = ListNode()
            if num1 < num2:
                curr.next.val = num1
                l1 = l1.next if l1 else l1
            else:
                curr.next.val = num2
                l2 = l2.next if l2 else l2
        return ans.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1 = ListtoListNode(l1)
l2 = ListtoListNode(l2)

print(ListNodetoList(l1))

# solution = Solution()
# print(solution.mergeTwoLists(l1, l2))