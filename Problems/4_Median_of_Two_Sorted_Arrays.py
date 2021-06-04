### Finally! I understood how to use binary search on this !!!!!!
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        len1 = len(nums1)
        len2 = len(nums2)
        left1 = 0
        right1 = len1

        while True:
            half1 = (left1 + right1)//2
            half2 = (len1 + len2 + 1) // 2 - half1

            maxLeft1 = nums1[half1 - 1] if half1 else float("-inf")
            minRight1 = nums1[half1] if half1 < len1 else float("inf")
            maxLeft2 = nums2[half2 - 1] if half2 else float("-inf")
            minRight2 = nums2[half2] if half2  < len2 else float("inf")

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len1 + len2) % 2 == 0:
                    return float((max(maxLeft1, maxLeft2) + min(minRight1, minRight2))/2)
                else:
                    return float(max(maxLeft1, maxLeft2))
            elif maxLeft1 > minRight2:
                right1 = half1 -1
            else:
                left1 = half1 + 1


solution = Solution()
nums1 = [1,3]
nums2 = [2]     

print(solution.findMedianSortedArrays(nums1, nums2))

######### Bad Solution #############
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         nums = nums1 + nums2
#         nums.sort()
#         total = len(nums)
#         index = total//2
#         if total % 2 == 1:
#             return float(nums[index])
#         else:
#             return float((nums[index] + nums[index-1])/2)

###### Bad Solition too (I tried to use binary search but I misunderstood it and do some idiot list operation  so I even made it worse LOL)
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         if len(nums1) < len(nums2):
#             short_nums, long_nums = nums1, nums2
#         else:
#             short_nums, long_nums = nums2, nums1
#         short_nums.append(float("inf"))
#         short_nums.insert(0, float("-inf"))
#         long_nums.append(float("inf"))
#         long_nums.insert(0, float("-inf"))
#         short_pointer = len(short_nums)
#         long_pointer = len(long_nums)
#         total_pointer = (short_pointer + long_pointer + 1)//2
#         short_pointer = (short_pointer)//2
#         long_pointer = total_pointer - short_pointer 
#         while True :
#             if long_nums[long_pointer - 1] > short_nums[short_pointer]:
#                 short_pointer += 1
#                 long_pointer -= 1
#             elif short_nums[short_pointer - 1] > long_nums[long_pointer]:
#                 short_pointer -= 1
#                 long_pointer += 1
#             if short_nums[short_pointer - 1] <= long_nums[long_pointer] and long_nums[long_pointer - 1] <= short_nums[short_pointer]:
#                 break
        
#         if (len(short_nums) + len(long_nums)) % 2 == 0:
#             return (max(short_nums[short_pointer - 1], long_nums[long_pointer - 1]) + min(short_nums[short_pointer], long_nums[long_pointer]))/2
#         else:
#             return max(short_nums[short_pointer - 1], long_nums[long_pointer - 1])