#include<iostream>
#include<string>
#include<math.h>

using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int total = 0;
        int power = 0;
        for(int i = columnTitle.length()-1; i>-1; i--){
            total += (columnTitle[i]-64)* pow(26, power);
            power++;
        }
        return total;
    }
};