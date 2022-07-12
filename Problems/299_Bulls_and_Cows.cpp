#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    string getHint(string secret, string guess) {
        int cntA = 0;
        int cntB = 0;
        vector<int> secretTable(10, 0);
        vector<int> guessTable(10, 0);
        for(int i=0; i<secret.size(); i++){
            if(secret[i]==guess[i]) cntA++;
            else{
                secretTable[secret[i]-'0']++;
                guessTable[guess[i]-'0']++;
            }
        }
        for(int i=0; i<10; i++){
            cntB += min(secretTable[i], guessTable[i]);
        }
        return to_string(cntA)+'A'+to_string(cntB)+'B';
    }
};