class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int maxScore = 0;
        int score = 0;
        int l = 0;
        int r = tokens.size() - 1;
        sort(tokens.begin(), tokens.end());
        while (l <= r) {
            if (power >= tokens[l]) {
                power -= tokens[l];
                ++score;
                maxScore = max(maxScore, score);
                ++l;
            } else if (score > 0) {
                power += tokens[r];
                --score;
                --r;
            } else {
                break;
            }
        }
        return maxScore;
    }
};