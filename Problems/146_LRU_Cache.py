from collections import deque

# cleanest solution
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.qu = deque()

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        self.qu.remove(key)
        self.qu.appendleft(key)
        return self.hashMap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.qu.remove(key)
        else:
            if len(self.qu) == self.capacity:
                popKey = self.qu.pop()
                self.hashMap.pop(popKey)
        self.hashMap[key] = value
        self.qu.appendleft(key)

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