class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        seen = {}  # key: c, val: False -> seen but not in the current search, True -> seen and it is in the current search
        res = []
        def dfs(c):
            """
            Return:
                True -> there is a loop, which is illegal
                False -> Legal
            """
            if c in seen:
                return seen[c]
            seen[c] = True
            for nc in adj[c]:
                if dfs(nc):
                    return True
            seen[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
