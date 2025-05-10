class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = sum(nums1)
        zero_cnt1 = Counter(nums1)[0]

        total2 = sum(nums2)
        zero_cnt2 = Counter(nums2)[0]

        if zero_cnt2 == 0 and total1 + zero_cnt1 > total2:
            return -1
        if zero_cnt1 == 0 and total2 + zero_cnt2 > total1:
            return -1
        return max(total1 + zero_cnt1, total2 + zero_cnt2)
