class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointS = 0
        for i in range(len(t)):
            if pointS==len(s):
                return True
            if t[i]==s[pointS]:
                pointS += 1
        return pointS==len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointS = 0
        for i in range(len(t)):
            if pointS==len(s):
                return True
            if t[i]==s[pointS]:
                pointS += 1
        if pointS==len(s):
            return True
        else:
            return False