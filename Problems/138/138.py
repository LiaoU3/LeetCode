"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        self.map[head] = Node(x=head.val)
        self.map[head].next = self.copyRandomList(head.next)
        self.map[head].random = self.copyRandomList(head.random)
        return self.map[head]
