# O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1


# O (n * log(n))
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(l, r, target):
            if l > r:
                return -1
            m = (l + r) // 2
            if numbers[m] == target:
                return m
            elif numbers[m] > target:
                return binary_search(l, m - 1, target)
            else:
                return binary_search(m + 1, r, target)
        
        for l in range(len(numbers) - 1):
            r = binary_search(l + 1, len(numbers) - 1, target - numbers[l])
            if r != -1:
                return [l + 1, r + 1]


# TLE O(n ^ 2)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for l in range(len(numbers) - 1):
            for r in range(l + 1, len(numbers)):
                if numbers[l] + numbers[r] < target:
                    continue
                elif numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                else:
                    break
