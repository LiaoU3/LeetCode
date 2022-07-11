from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        lengthS = len(s)
        lengthP = len(p)
        if lengthS<lengthP:
            return res

        alphaP = [0]*26
        for c in p:
            alphaP[ord(c)-ord('a')] += 1
            
        alphaS = [0]*26
        for i in range(lengthP):
            alphaS[ord(s[i])-ord('a')] += 1
        
        if alphaS==alphaP:
            res.append(0)
        for i in range(1, lengthS-lengthP+1):
            alphaS[ord(s[i-1])-ord('a')]-=1
            alphaS[ord(s[i+lengthP-1])-ord('a')] += 1
            if alphaS==alphaP:
                res.append(i)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "abab"
    p = "ab"
    print(sol.findAnagrams(s, p))