from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()  # (val, index)
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        res = [q[0][0]]
        for i in range(k, len(nums)):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
            if q[0][1] <= i - k:
                q.popleft()
            res.append(q[0][0])

        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # Keep it monotonic decreasing by value
        q = deque()  # (value, index)

        for i in range(len(nums)):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))

            if q[0][1] <= i - k:
                q.popleft()
            
            if i + 1 >= k:
                res.append(q[0][0])
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = []
        res = []

        for i in range(len(nums)):
            while hp and hp[0][1] <= i - k:
                heappop(hp)
            if not hp or nums[i] > -hp[0][0]:
                heappush(hp, (-nums[i], i))
            if i < k - 1:
                continue
            res.append(-hp[0][0])
        return res

# Not fast enough
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         hp = []
#         res = []

#         for i in range(len(nums)):
#             heappush(hp, (-nums[i], i))
#             if i < k - 1:
#                 continue
#             while hp[0][1] <= i - k:
#                 heappop(hp)
#             res.append(-hp[0][0])
#         return res

s = Solution()
nums = [1,3,1,2,0,5]