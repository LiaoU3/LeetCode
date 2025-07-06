class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        n2 = self.nums2[index]
        self.counter[n2] -= 1
        self.counter[n2 + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for n1 in self.nums1:
            diff = tot - n1
            res += self.counter[diff]
        return res


# TLE
    # def __init__(self, nums1: List[int], nums2: List[int]):
    #     self.counter = defaultdict(int)  # key: total, val: count
    #     self.nums1 = nums1
    #     self.nums2 = nums2
    #     for n1 in nums1:
    #         for n2 in nums2:
    #             self.counter[n1 + n2] += 1

    # def add(self, index: int, val: int) -> None:
    #     n2 = self.nums2[index]
    #     for n1 in self.nums1:
    #         self.counter[n1 + n2] -= 1
    #         self.counter[n1 + n2 + val] += 1
    #     self.nums2[index] += val

    # def count(self, tot: int) -> int:
    #     return self.counter[tot]
