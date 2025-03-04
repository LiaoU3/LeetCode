from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        
        def is_greater(t):
            for n1, n2 in zip(t, target):
                if n1 > n2:
                    return True
            return False

        for trip in triplets:
            if is_greater(trip):
                continue
            for i in range(3):
                curr[i] = max(curr[i], trip[i])
            if curr == target:
                return True
        return False

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()

        def check_exceed(triplet):
            for i in range(3):
                if triplet[i] > target[i]:
                    return True
            return False
        
        def update_triplet(original, update):
            for i in range(3):
                original[i] = max(original[i], update[i])

        def backtrack(curr, i):
            if curr == target:
                return True
            if i == len(triplets):
                return False
            if not check_exceed(triplets[i]):
                update_triplet(curr, triplets[i])
            return backtrack(curr, i + 1)

        return backtrack([0, 0, 0], 0)

s = Solution()
print(s.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))