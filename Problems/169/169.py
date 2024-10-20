# Time Complexity O(N), Space Complexity O(1)
# Cleaner solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = None
        for num in nums:
            if cnt == 0:
                res = num
            if num == res:
                cnt += 1
            else:
                cnt -= 1
        return res

# Time Complexity O(N), Space Complexity O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != res:
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                res = nums[i]
                cnt = 1
        return res

# Time Complexity O(N), Space Complexity O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)  # key: num, value: frequency
        threshold = len(nums) // 2
        for num in nums:
            hash_map[num] += 1
            if hash_map[num] > threshold:
                return num