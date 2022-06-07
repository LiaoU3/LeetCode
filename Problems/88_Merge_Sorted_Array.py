from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        point = m+n-1
        m -= 1
        n -=1
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[point] = nums1[m]
                m -= 1
            else:
                nums1[point] = nums2[n]
                n -=1
            point -= 1
        if n>=0:
            nums1[:n+1] = nums2[:n+1]

if __name__ =="__main__":
    sol = Solution()
    nums1 = [0]

    m = 0

    nums2 = [1]

    n = 1
    print(sol.merge(nums1, m, nums2, n))