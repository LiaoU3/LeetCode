#include<string>

using namespace std;
class Solution {
public:
    int minPartitions(string n) {
        int max_digit = 0;
        for(auto c: n){
            if(c-'0'>max_digit) max_digit = c-'0';
        }
        return max_digit;
    }
};