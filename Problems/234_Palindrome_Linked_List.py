# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        cnt = 0
        pre = None
        while fast:
            fast = fast.next
            if cnt % 2:
                nxt = slow.next
                slow.next = pre
                pre = slow
                slow = nxt
            cnt += 1

        if cnt % 2:
            fast = slow.next
        else:
            fast = slow
        while pre:
            if pre.val != fast.val:
                return False
            pre = pre.next
            fast = fast.next
        return True


# Time Complexity : O(n), Space Complexity : O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True