class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        def is_valid(threshold):
            cnt = 0
            i = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2
                    if cnt == p:
                        return True
                else:
                    i += 1
            return False

        l, r = 0, nums[-1] - nums[0]
        res = nums[-1] - nums[0]
        while l <= r:
            m = l + (r - l) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
