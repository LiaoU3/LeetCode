# using one dict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        hm = Counter(magazine)
        for c in ransomNote:
            hm[c] -= 1
            if hm[c] < 0:
                return False
        return True

#using list
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        ransomTable = [0] * 26
        magazineTable = [0] * 26
        for c in magazine:
            magazineTable[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            i = ord(c) - ord('a')
            ransomTable[i] += 1

        for i in range(26):
            if ransomTable[i] and ransomTable[i] > magazineTable[i]:
                return False
        return True

# using hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        hm1 = Counter(ransomNote)
        hm2 = Counter(magazine)
        
        for key in hm1:
            if hm1[key] > hm2[key]:
                return False
        return True