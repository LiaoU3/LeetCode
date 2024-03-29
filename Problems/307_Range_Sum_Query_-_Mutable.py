class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumUp = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.sumUp += val-self.nums[index]
        self.nums[index]=val

    def sumRange(self, left: int, right: int) -> int:
        if right-left>len(self.nums):
            return sum(self.nums[left:right+1])
        else:
            return self.sumUp-sum(self.nums[:left])-sum(self.nums[right+1:])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)