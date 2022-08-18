from typing import List
from collections import Counter, defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        target = (len(arr) + 1) // 2
        res = 0
        for _, cnt in c.most_common():
            target -= cnt
            res += 1
            if target <= 0:
                return res
        return res

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        target = (len(arr) + 1) // 2
        res = 0
        for _, cnt in c.most_common():
            target -= cnt
            res += 1
            if target <= 0:
                return res
        return res

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hm = defaultdict(int)
        target = (len(arr) + 1) // 2
        for num in arr:
            hm[num] += 1
        
        counts = list(hm.values())
        counts.sort(reverse = True)
        res = 0
        total = 0
        for cnt in counts:
            total += cnt
            res += 1
            if total >= target:
                return res
        return res