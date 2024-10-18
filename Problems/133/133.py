"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2new = {}
        def dfs(node):
            if node in old2new:
                return old2new[node]
            clone = Node(node.val)
            old2new[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hash_map = {}  # old: new
        seen = set()

        def dfs(node):
            if node.val in seen:
                return
            seen.add(node.val)
            clone = Node(node.val)
            hash_map[node] = clone
            for neighbor in node.neighbors:
                dfs(neighbor)
                hash_map[node].neighbors.append(hash_map[neighbor])
        dfs(node)
        return hash_map[node]