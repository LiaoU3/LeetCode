#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

class Solution {
public:
    bool isPossible(vector<int>& target) {
        if(target.size()==1) return target[0]==1;
        priority_queue<int> pq;
        long total = 0;
        for(auto num:target){
            pq.push(num);
            total += num;
        }
        while(true){
            int largest = pq.top();
            pq.pop();
            if(largest==1) return true;
            total -= largest;
            int remain = (largest-1) % total + 1;
            if (remain<1 || largest==remain) return false;
            pq.push(remain);
            total += remain;
        }
    }
};