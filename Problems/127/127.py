# Slow  O(L² * N)  N: the number of words, L: the length of a word
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = defaultdict(list)  # e.g. key: h*t, val: [hot, hit, ...]
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i + 1:]
                d[s].append(word)

        res = 1
        seen = set([beginWord])
        q = deque([beginWord])
        while q:
            length = len(q)
            for _ in range(length):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i + 1:]
                    for target in d[s]:
                        if target not in seen:
                            q.append(target)
                            seen.add(target)
            res += 1
        return 0

# Slow  O(N² * L)  N: the number of words, L: the length of a word
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def is_legal(w1, w2):
            cnt = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    cnt += 1
                if cnt > 1:
                    return False
            return True if cnt == 1 else False

        seen = set([beginWord])
        q = deque([beginWord])

        res = 1
        while q:
            length = len(q)
            for _ in range(length):
                word = q.popleft()
                if word == endWord:
                    return res
                for match in wordList:
                    if match in seen:
                        continue
                    if is_legal(word, match):
                        q.append(match)
                        seen.add(match)
            res += 1
        
        return 0