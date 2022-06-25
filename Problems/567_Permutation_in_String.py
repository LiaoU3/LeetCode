class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        window = len(s1)
        alpha_table_target = [0]*26
        for c in s1:
            alpha_table_target[ord(c)-ord('a')] += 1

        alpha_table_current = [0]*26
        for i in range(window):
            alpha_table_current[ord(s2[i])-ord('a')] += 1

        if alpha_table_current == alpha_table_target:
            return True
        for i in range(window, len(s2)):
            alpha_table_current[ord(s2[i])-ord('a')]+=1
            alpha_table_current[ord(s2[i-window])-ord('a')]-=1
            if alpha_table_current == alpha_table_target:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s1 = "a"
    s2 = "ab"
    # s2 = "eidbaooo"
    print(sol.checkInclusion(s1, s2))