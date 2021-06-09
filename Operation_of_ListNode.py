# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a ListNode from a list
def ListtoListNode(ls = []):
    ret = ListNode()
    curr = ret
    for num in ls:
        curr.val = num
        curr.next = ListNode()
        curr = curr.next
    curr.next = None
    return ret

# Create a list from a ListNode
def ListNodetoList(ln = ListNode()):
    ret = []
    while ln.next != None:
        ret.append(ln.val)
        ln = ln.next
    return ret