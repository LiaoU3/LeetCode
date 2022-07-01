# without using dict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = [-1] * 127
        tMap = [-1] * 127
        for i in range(len(s)):
            if sMap[ord(s[i])]== -1:
                if tMap[ord(t[i])] != -1:
                    return False
                sMap[ord(s[i])] = ord(t[i])
                tMap[ord(t[i])] = ord(s[i])
            else:
                if tMap[ord(t[i])] != ord(s[i]):
                    return False
                
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphaMap = {}
        for i in range(len(s)):
            if s[i] in alphaMap:
                if t[i] != alphaMap[s[i]]:
                    return False
            else:
                if t[i] in alphaMap.values():
                    return False
                alphaMap[s[i]] = t[i]
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "badc"
    t = "baba"
    print(sol.isIsomorphic(s, t))