class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        seen = set()
        seen.add(tops[0])
        seen.add(bottoms[0])
        for t, b in zip(tops[1:], bottoms[1:]):
            new_seen = set()
            for num in seen:
                if num == t or num == b:
                    new_seen.add(num)
            seen = new_seen
            if len(seen) == 0:
                return -1

        num = seen.pop()
        cnt1 = 0
        for t in tops:
            if num != t:
                cnt1 += 1
        cnt2 = 0
        for b in bottoms:
            if num != b:
                cnt2 += 1

        return min(cnt1, len(tops) - cnt1, cnt2, len(tops) - cnt2)
