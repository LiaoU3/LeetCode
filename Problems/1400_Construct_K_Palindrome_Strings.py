class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        num_set = set()
        for c in s:
            if c not in num_set:
                num_set.add(c)
            else:
                num_set.remove(c)
        if len(num_set) > k:
            return False
        return True