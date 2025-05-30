from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def dfs(seen, ls, node):
            if node == -1:
                return
            if node in seen:
                return
            seen.add(node)
            ls.append(node)
            dfs(seen, ls, edges[node])

        ls1 = []
        ls2 = []

        dfs(set(), ls1, node1)
        dfs(set(), ls2, node2)
        print(ls1)
        print(ls2)
        seen1 = set()
        seen2 = set()

        i1 = 0
        i2 = 0
        res = []
        while i1 < len(ls1) or i2 < len(ls2):
            n1 = ls1[i1] if i1 < len(ls1) else ls1[-1]
            n2 = ls2[i2] if i2 < len(ls2) else ls2[-1]

            seen1.add(n1)
            seen2.add(n2)

            if n1 in seen2:
                res.append(n1)
            if n2 in seen1:
                res.append(n2)
            if res:
                return min(res)
            i1 += 1
            i2 += 1

        return -1
