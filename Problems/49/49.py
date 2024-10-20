class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) # key: tuple, value: list of str
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord("a")] += 1
            hash_map[tuple(cnt)].append(s)
        res = []
        for key in hash_map:
            res.append(hash_map[key])
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) # key: list, value: list of str
        for s in strs:
            ls = []
            for c in s:
                ls.append(c)
            ls.sort()
            key = "".join(ls)
            hash_map[key].append(s)
        res = []
        for key in hash_map:
            res.append(hash_map[key])
        return res