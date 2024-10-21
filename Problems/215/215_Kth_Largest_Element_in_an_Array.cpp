#include<vector>
#include<iostream>
#include<queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for(int i=0; i<k; i++){
            pq.push(INT_MIN);
        }
        for(auto num: nums){
            pq.push(num);
            pq.pop();
        }
        return pq.top();
    }
};