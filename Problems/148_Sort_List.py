# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# MergeSort solution
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            right = findMiddle(head)
            left = head
            left = mergeSort(left)
            right = mergeSort(right)
            newHead = merge(left, right)
            return newHead

        def findMiddle(head):
            slow = head
            fast = head
            
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            res = slow.next
            slow.next = None
            return res

        def merge(left, right):
            dummy = ListNode()
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if not left:
                curr.next = right
            else:
                curr.next = left
            return dummy.next
        
        head = mergeSort(head)
        return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums.sort()
        curr = head
        i = 0
        while curr:
            curr.val = nums[i]
            i += 1
            curr = curr.next
        return head