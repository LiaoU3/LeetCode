class Solution:
    def minDeletions(self, s: str) -> int:
        freq_table = [0]*26
        for c in s:
            freq_table[ord(c)-ord('a')] += 1
        freq_table.sort(reverse=True)
        freq_set = set()
        
        delete_cnt = 0
        for freq in freq_table:
            if freq==0:
                break
            while freq in freq_set:
                freq -= 1
                delete_cnt += 1
            if freq:
                freq_set.add(freq)
        return delete_cnt

if __name__ == '__main__':
    sol = Solution()
    s = "bbcebab"
    print(sol.minDeletions(s))