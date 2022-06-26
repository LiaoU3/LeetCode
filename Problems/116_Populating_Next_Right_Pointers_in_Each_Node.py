from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        qu = deque([root])
        while qu:
            q_len = len(qu)
            for i in range(q_len):
                curr = qu.popleft()
                if i<q_len-1:
                    curr.next = qu[0]
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        return root