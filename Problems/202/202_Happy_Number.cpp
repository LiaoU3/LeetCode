class Solution {
public:
    bool isHappy(int n){
        unordered_set<int> seen;
        while(n!=1){
            int newN = 0;
            while(n){
                newN += pow(n%10, 2);
                n /=10;
            }
            n = newN;
            if(seen.count(n)) return false;
            seen.insert(n);
        }
        return true;
    }
};