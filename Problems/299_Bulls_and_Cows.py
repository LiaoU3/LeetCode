class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretTable = [0]*10
        guessTable = [0]*10
        cntA = 0
        cntB = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                cntA += 1
            else:
                secretTable[secret[i]] += 1
                guessTable[guess[i]] += 1
        for i in range(10):
            cntB += min(secretTable[i], guessTable[i])
        return str(cntA)+'A'+str(cntB)+'B'