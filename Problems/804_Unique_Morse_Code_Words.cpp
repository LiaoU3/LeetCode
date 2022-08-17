class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> table = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string> transform;
        
        for (auto word : words) {
            string s;
            for (auto c : word) {
                s += table[c - 'a'];
            }
            transform.insert(s);
        }
        return transform.size();
    }
};