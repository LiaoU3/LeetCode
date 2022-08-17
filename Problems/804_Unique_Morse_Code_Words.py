class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = {''.join(table[ord(c) - ord('a')] for c in word) for word in words}
        return len(transform)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = set()
        for word in words:
            s = ''.join(table[ord(c) - ord('a')] for c in word)
            transform.add(s)
        return len(transform)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = set()
        for word in words:
            s = ""
            for c in word:
                s += table[ord(c) - ord('a')]
            transform.add(s)
        return len(transform)