# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Operation_of_ListNode import *
from typing import Optional
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]
            if left + 1 == right:
                return merge2list(lists[left], lists[right])
            
            middle = left + (right-left)//2
            l1 = merge(left, middle)
            l2 = merge(middle + 1, right)
            return merge2list(l1, l2)

        def merge2list(node1, node2):
            if node1 is None and node2 is None:
                return None
            val1 = node1.val if node1 else float("Inf")
            val2 = node2.val if node2 else float("Inf")
            if val1 < val2:
                node = ListNode(val1)
                node1 = node1.next
            else:
                node = ListNode(val2)
                node2 = node2.next
            node.next = merge2list(node1, node2)
            return node
        return merge(0, len(lists)-1)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]
            if left + 1 == right:
                return mergeTwoLists(lists[left], lists[right])
            
            middle = left + (right-left)//2
            l1 = merge(left, middle)
            l2 = merge(middle + 1, right)
            return mergeTwoLists(l1, l2)

        # from problem 21 merge two sorted list
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            result = ListNode()
            curr = result
            while l1 or l2:
                num1 = l1.val if l1 else 10001
                num2 = l2.val if l2 else 10001
                curr.next = ListNode()
                if num1 < num2:
                    curr.next.val = num1
                    l1 = l1.next if l1 else l1
                else:
                    curr.next.val = num2
                    l2 = l2.next if l2 else l2
                curr = curr.next
            return result.next

        return merge(0, len(lists)-1)

# Slow
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2lists(l1, l2):
            dummy = curr = ListNode()
            while l1 or l2:
                v1 = l1.val if l1 else float("Inf")
                v2 = l2.val if l2 else float("Inf")
                if v1 < v2:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            return dummy.next
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2lists(res, lists[i])
        return res

# Slow
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def sort():
            min_node = (ListNode(float("Inf")), -1)
            for i, node in enumerate(lists):
                if node and node.val < min_node[0].val:
                    min_node = (node, i)
            if min_node[1] == -1:
                return None
            lists[min_node[1]] = lists[min_node[1]].next
            min_node[0].next = sort()
            return min_node[0]
        return sort()


def main():
    lists = [[1,4,5],[1,3,4],[2,6]]
    new_lists_node = []
    for ls in lists:
        new_lists_node.append(List2Node(ls))

    for ls in new_lists_node:
        print(Node2List(ls))
    solution = Solution()
    print(Node2List(solution.mergeKLists(new_lists_node)))

if __name__ == '__main__':
    main()