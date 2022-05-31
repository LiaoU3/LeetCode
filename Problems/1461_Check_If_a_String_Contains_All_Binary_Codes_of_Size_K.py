class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        start = 0
        end = k-1
        for _ in range(len(s)):
            if end < len(s):
                codes.add(s[start:end+1])
            start += 1
            end +=1
        if len(codes) == 2**k:
            return True
        else:
            return False
    
if __name__ == '__main__':
    s = "00110110"
    k = 2
    sol = Solution()
    print(sol.hasAllCodes(s, k))