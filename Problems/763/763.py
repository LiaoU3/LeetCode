from collections import defaultdict
from typing import List

# O(N) but faster
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        end = 0
        start = -1
        res = []
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                res.append(end - start)
                start = end
        return res


# O(N)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = [[-1, -1] for _ in range(26)]
        for i, c in enumerate(s):
            j = ord(c) - ord("a")
            if alpha[j][0] == -1:
                alpha[j][0] = i
            else:
                alpha[j][1] = i
        start = 0
        res = []
        for i in range(len(s)):
            for c in alpha:
                if c[0] <= i < c[1]:
                    break
            else:
                res.append(i - start + 1)
                start = i + 1
        return res

# O(N*log(N))
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = defaultdict(list)
        for i, c in enumerate(s):
            hash_map[c].append(i)

        intervals = []
        for c in hash_map:
            intervals.append([hash_map[c][0], hash_map[c][-1]])
        intervals.sort()

        part = [[-1, -1]]
        for i in range(len(intervals)):
            if intervals[i][0] < part[-1][1]:
                part[-1][1] = max(part[-1][1], intervals[i][1])
            else:
                part.append(intervals[i])

        res = []
        for start, end in part[1:]:
            res.append(end - start + 1)

        return res

s = "ababcbacadefegdehijhklij"
sol = Solution()
print(sol.partitionLabels(s))
