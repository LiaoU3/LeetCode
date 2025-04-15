class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_cnt = [0] * (n + 1)
        trust_someone = [False] * (n + 1)

        for u, v in trust:
            trust_cnt[v] += 1
            trust_someone[u] = True

        for i in range(1, n + 1):
            if not trust_someone[i] and trust_cnt[i] == n - 1:
                return i
        return -1
