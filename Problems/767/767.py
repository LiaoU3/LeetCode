class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        max_cnt = max(counter.values())
        if max_cnt > (len(s) + 1) // 2:
            return ""

        hp = []
        for c, freq in counter.items():
            heappush(hp, (-freq, c))

        res = []
        while len(hp) > 1:
            freq1, c1 = heappop(hp)
            freq2, c2 = heappop(hp)

            res.extend([c1, c2])

            if freq1 < -1:
                heappush(hp, (freq1 + 1, c1))

            if freq2 < -1:
                heappush(hp, (freq2 + 1, c2))
        if hp:
            freq, c = heapq.heappop(hp)
            # if -freq > 1:
            #     return ""
            res.append(c)

        return "".join(res)
