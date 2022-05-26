from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m-1
        pointer2 = n-1
        pointer  = len(nums1)-1
        while pointer1>=0 and pointer2>=0:
            if nums1[pointer1]>nums2[pointer2]:
                nums1[pointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1
            pointer -= 1
        if pointer2 > pointer1:
            nums1[:pointer+1] = nums2[:pointer2+1]
        return nums1

if __name__ =="__main__":
    sol = Solution()
    nums1 = [0]

    m = 0

    nums2 = [1]

    n = 1
    print(sol.merge(nums1, m, nums2, n))