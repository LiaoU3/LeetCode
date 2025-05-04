class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        res = 0
        for n1, n2 in dominoes:
            if n2 < n1:
                n1, n2 = n2, n1
            counter[(n1, n2)] += 1
            res += counter[(n1, n2)] - 1
        
        return res

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        for n1, n2 in dominoes:
            if n2 < n1:
                n1, n2 = n2, n1
            counter[(n1, n2)] += 1

        res = 0
        for cnt in counter.values():
            for i in range(1, cnt):
                res += i

        return res
