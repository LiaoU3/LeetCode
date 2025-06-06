class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0] * 26
        for c in s:
            table[ord(c) - ord("a")] += 1

        for c in t:
            table[ord(c) - ord("a")] -= 1
            if table[ord(c) - ord("a")] < 0:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = [0] * 26
        for cs, ct in zip(s, t):
            alphabet[ord(cs) - ord("a")] += 1
            alphabet[ord(ct) - ord("a")] -= 1
        for count in alphabet:
            if count:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = defaultdict(int)
        for c in s:
            hash_map[c] += 1
        for c in t:
            if c not in hash_map:
                return False
            hash_map[c] -= 1
            if hash_map[c] < 0:
                return False
        return True

# using only one list
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         table = [0]*26

#         for c1, c2 in zip(s, t):
#             table[ord(c1) - ord('a')] += 1
#             table[ord(c2) - ord('a')] -= 1            

#         for i in range(26):
#             if table[i]:
#                 return False
#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         sTable = [0]*26
#         tTable = [0]*26

#         for c1, c2 in zip(s, t):
#             sTable[ord(c1) - ord('a')] += 1
#             tTable[ord(c2) - ord('a')] += 1            

#         for i in range(26):
#             if sTable[i] != tTable[i]:
#                 return False
#         return True
