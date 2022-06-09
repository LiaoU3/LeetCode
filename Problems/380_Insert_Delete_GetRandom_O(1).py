import random

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        
        self.hash_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        self.hash_map[self.num_list[-1]] = self.hash_map[val]
        self.num_list[-1], self.num_list[self.hash_map[val]] = self.num_list[self.hash_map[val]], self.num_list[-1]
        self.num_list.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()