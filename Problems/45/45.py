
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            new_r = r
            for i in range(l, r + 1):
                new_r = max(new_r,  i + nums[i])
            l = r + 1
            r = new_r
            res += 1
        return res


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