class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p1 = p2 = 0
        for p3 in range(len(s3)):
            if p1<len(s1) and s3[p3]==s1[p1]:
                p1 += 1
            elif p2<len(s2) and s3[p3]==s2[p2]:
                p2 += 1
            elif p3 != len(s3)-1:
                return False
                
        return True

if __name__ == '__main__':
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(sol.isInterleave(s1, s2, s3))