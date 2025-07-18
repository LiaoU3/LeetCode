class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        priorities = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))
            if w1[: min_len] == w2[: min_len] and len(w1) > len(w2):
                return False
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if priorities[w1[j]] > priorities[w2[j]]:
                        return False
                    break

        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        before = defaultdict(set)
        for i in range(len(order)):
            for j in range(i):
                before[order[i]].add(order[j])
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    if c1 not in before[c2]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True
