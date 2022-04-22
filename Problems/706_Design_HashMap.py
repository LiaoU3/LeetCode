class MyHashMap:

    def __init__(self):
        self.map = []
    
    def _find_index(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return i
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        index = self._find_index(key)
        if index == -1 :
            self.map.append([key, value])
        else:
            self.map[index][1] = value
            
    def get(self, key: int) -> int:
        index = self._find_index(key)
        if index != -1 :
            return self.map[index][1]
        else:
            return -1


    def remove(self, key: int) -> None:
        index = self._find_index(key)
        if index != -1 :    
            self.map.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Of course you could use dict in python 
# But I think it's kinda like cheating
# class MyHashMap:

#     def __init__(self):
#         self.map = {}

#     def put(self, key: int, value: int) -> None:
#         self.map[key] = value

#     def get(self, key: int) -> int:
#         if key in self.map:
#             return self.map[key]
#         else:
#             return -1

#     def remove(self, key: int) -> None:
#         if self.get(key) != -1:
#             del self.map[key]