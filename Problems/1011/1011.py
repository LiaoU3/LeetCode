class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        self.res = r
        def binary_search(l, r):
            if l > r:
                return
            m = (l + r) // 2
            if can_put(m):
                self.res = min(self.res, m)
                binary_search(l, m - 1)
            else:
                binary_search(m + 1, r)
        
        def can_put(capacity):
            curr_load = 0
            curr_days = 0
            for w in weights:
                if curr_load + w > capacity:
                    curr_days += 1
                    curr_load = 0
                curr_load += w
            return curr_days < days
        binary_search(l, r)
        return self.res