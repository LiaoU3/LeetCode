class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    curr.append(num)
                    backtrack(curr)
                    counter[num] += 1
                    curr.pop()

        backtrack([])
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        res = set()
        def backtrack(curr):
            if len(curr) == len(nums):
                res.add(tuple(curr))
                return
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    curr.append(nums[i])
                    backtrack(curr)
                    used.remove(i)
                    curr.pop()

        backtrack([])
        return list(res)
