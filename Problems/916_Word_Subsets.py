class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def createTable(word: str) -> None:
            table = [0]*26
            for c in word:
                table[ord(c) - ord('a')] += 1
            return table

        target = [0]*26
        for word2 in words2:
            tmp = [0]*26
            for c in word2:
                tmp[ord(c) - ord('a')] += 1
            for i in range(26):
                if target[i]<tmp[i]:
                    target[i] = tmp[i]
        res = []
        for word1 in words1:
            condidate = createTable(word1)
            for i in range(26):
                if condidate[i]<target[i]:
                    break
            else:
                res.append(word1)
        return res