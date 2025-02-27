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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        table1 = [0] * 26
        table2 = [0] * 26

        def is_permutation():
            for i in range(26):
                if table1[i] != table2[i]:
                    return False
            return True

        for i in range(len(s1)):
            table1[ord(s1[i]) - ord('a')] += 1
            table2[ord(s2[i]) - ord('a')] += 1

        if is_permutation():
            return True
        for i in range(len(s1), len(s2)):
            table2[ord(s2[i]) - ord('a')] += 1
            table2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if is_permutation():
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s1 = "a"
    # s2 = "ab"
    s2 = "eidbaooo"
    print(sol.checkInclusion(s1, s2))