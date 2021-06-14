class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s_set = set()
        for c in sentence:
            s_set.add(c)
            if len(s_set) == 26:
                return True
        return len(s_set) == 26