class Solution:
    def searchInsert(self, nums, target) -> int:
        start = 0
        end   = len(nums)
        index = (end + start)//2
        flag = 0
        while True:
            prev_index = index
            index = (end + start)//2
            num = nums[index]
            if prev_index == index :
                flag += 1
                if flag == 2:
                    if target < num:
                        return index
                    else:
                        return index + 1
            if num == target:
                return index
            elif num < target:
                start = index 
            else:
                end = index 

solution = Solution()
nums = [1, 2, 4, 6, 7]
target = 3
print(solution.searchInsert(nums, target))