class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}
        hp = []
        for word in words:
            if word in hashMap:
                hashMap[word] += 1
            else:
                hashMap[word] = 0
        
        for word, count in hashMap.items():
            heapq.heappush(hp, (-count, word))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(hp)[1])
        return res