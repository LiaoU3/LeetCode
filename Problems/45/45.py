
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        max_end = 0
        for i in range(len(nums) - 1):
            max_end = max(max_end, i + nums[i])
            if i == curr_end:
                jump += 1
                curr_end = max_end
        return jump


# Slow
class Solution:
    def jump(self, nums: List[int]) -> int:
        seen = set()
        q = deque([(0, 0)])

        while q:
            i, step = q.popleft()
            if i in seen:
                continue
            seen.add(i)
            if i >= len(nums) - 1:
                return step
            for j in range(1, nums[i] + 1):
                q.append((i + j, step + 1))
        return -1

# Slow O(N**2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cache = {}
        def backtrack(i):
            if i >= len(nums) - 1:
                cache[i] = 1
                return 0
            if i in cache:
                return cache[i]
            min_steps = float("Inf")
            for j in range(i + nums[i], i, -1):
                min_steps = min(min_steps, backtrack(j))
            cache[i] = 1 + min_steps
            return cache[i]

        return backtrack(0)

sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))