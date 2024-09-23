# from collections import deque


# Time Complexity O(N)
class Node():
    def __init__(self, key: int = 0, val: int = 0, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}  # key: node
        self.l = Node()
        self.r = Node()
        self.l.right = self.r
        self.r.left = self.l

    def pop(self) -> Node:
        """Pop a node from the right"""
        node_rightest = self.r.left
        node_rightest_left = node_rightest.left
        node_rightest_left.right = self.r
        self.r.left = node_rightest_left
        return node_rightest

    def appendleft(self, node: Node) -> None:
        """Append a node from the left"""
        # Connect node to the leftest node
        node_leftest = self.l.right
        node_leftest.left = node
        node.right = node_leftest
        # Connect node to l
        node.left = self.l
        self.l.right = node

    def remove(self, node: Node):
        """Remove a node from the linked list"""
        left = node.left
        right = node.right
        left.right = right
        right.left = left

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.remove(node)
        # Move node to the left
        self.appendleft(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove(node)
        else:
            if len(self.hash_map) == self.capacity:
                node_to_be_removed = self.pop()
                del self.hash_map[node_to_be_removed.key]
        node = Node(key, value)
        self.hash_map[key] = node
        self.appendleft(node)

# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cleanest solution
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashMap = {}
#         self.qu = deque()

#     def get(self, key: int) -> int:
#         if key not in self.hashMap:
#             return -1
#         self.qu.remove(key)
#         self.qu.appendleft(key)
#         return self.hashMap[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.hashMap:
#             self.qu.remove(key)
#         else:
#             if len(self.qu) == self.capacity:
#                 popKey = self.qu.pop()
#                 self.hashMap.pop(popKey)
#         self.hashMap[key] = value
#         self.qu.appendleft(key)

# cleaner
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashMap = {}
#         self.qu = deque()

#     def get(self, key: int) -> int:
#         if key not in self.hashMap:
#             return -1
#         self.qu.remove(key)
#         self.qu.appendleft(key)
#         return self.hashMap[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.hashMap:
#             self.hashMap[key] = value
#             self.qu.remove(key)
#             self.qu.appendleft(key)
#         else:
#             if len(self.qu) == self.capacity:
#                 popKey = self.qu.pop()
#                 self.qu.appendleft(key)
#                 self.hashMap.pop(popKey)
#                 self.hashMap[key] = value
#             else:
#                 self.hashMap[key] = value
#                 self.qu.appendleft(key)

# redundant
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashMap = {}
#         self.qu = deque()

#     def get(self, key: int) -> int:
#         if key not in self.hashMap:
#             return -1
#         self.qu.remove(key)
#         self.qu.appendleft(key)
#         return self.hashMap[key]

#     def put(self, key: int, value: int) -> None:
#         if len(self.qu) == self.capacity:
#             if key in self.hashMap:
#                 self.hashMap[key] = value
#                 self.qu.remove(key)
#                 self.qu.appendleft(key)
#             else:
#                 popKey = self.qu.pop()
#                 self.qu.appendleft(key)
#                 self.hashMap.pop(popKey)
#                 self.hashMap[key] = value
#         else:
#             if key in self.hashMap:
#                 self.hashMap[key] = value
#                 self.qu.remove(key)
#                 self.qu.appendleft(key)
#             else:
#                 self.hashMap[key] = value
#                 self.qu.appendleft(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)