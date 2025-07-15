class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        for c in word:
            if c.isalpha():
                if c in "aeiouAEIOU":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isnumeric():
                return False
        return has_vowel and has_consonant
