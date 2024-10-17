class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + str(len(s)) + "#" + s
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length_str = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                length_str += s[j]
            length = int(length_str)
            res.append(s[i + len(length_str) + 1: i + len(length_str) + 1 + length])
            i = i + len(length_str) + 1 + length
            print(res)
        return res