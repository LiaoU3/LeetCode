class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)

        for s in strs:
            curr = [0] * 26
            for c in s:
                curr[ord(c) - ord("a")] += 1
            seen[tuple(curr)].append(s)

        return list(seen.values())

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