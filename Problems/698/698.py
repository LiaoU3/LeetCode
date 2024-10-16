class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        nums.sort(reverse=True)
        target = total // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j]:
                    continue
                if subsetSum + nums[j] > target:
                    continue
                # If nums[j] == nums[j - 1] and nums[j - 1] is not used, then we know that this is also not going to be used
                if j > 0 and not used[j - 1] and nums[j] == nums[j - 1]:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
        return backtrack(0, k, 0)