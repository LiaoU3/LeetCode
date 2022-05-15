# Definition for singly-linked list.
from operator import add


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a ListNode from a list
def List2Node(ls = []):
    ret = ListNode()
    curr = ret
    for num in ls:
        curr.next = ListNode(num)
        curr = curr.next
    curr.next = None
    return ret.next

# Create a list from a ListNode
def Node2List(ln = ListNode()):
    ret = []
    while ln.next != None:
        ret.append(ln.val)
        ln = ln.next
    return ret