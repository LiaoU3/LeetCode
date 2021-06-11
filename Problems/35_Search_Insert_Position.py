# a clear way to do this
class Solution:
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]== target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l


#### Too redundant
# class Solution:
#     def searchInsert(self, nums, target) -> int:
#         start = 0
#         end   = len(nums)
#         index = (end + start)//2
#         flag = 0
#         while True:
#             prev_index = index
#             index = (end + start)//2
#             num = nums[index]
#             if prev_index == index :
#                 flag += 1
#                 if flag == 2:
#                     if target < num:
#                         return index
#                     else:
#                         return index + 1
#             if num == target:
#                 return index
#             elif num < target:
#                 start = index 
#             else:
#                 end = index 

solution = Solution()
nums = [1, 2, 4, 6, 7, 9, 10, 12, 15]
target = 3
print(solution.searchInsert(nums, target))