class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point = 0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if s[point] == t[i]:
                point += 1
                if point ==len(s):
                    return True
        return False

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