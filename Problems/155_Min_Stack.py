class MinStack:

    def __init__(self):
        self.length = 0
        self.min = float('Inf')
        self.stack = [0]*3*10**4

    def push(self, val: int) -> None:
        self.stack[self.length] = val
        self.length += 1
        if self.min > val:
            self.min = val
    def pop(self) -> None:
        if self.stack[self.length - 1] == self.min:
            self.min = float('Inf')
            for i in range(self.length-1):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]
        self.length -= 1
    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()