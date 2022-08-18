#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> hm;
        for (auto num : arr) {
            ++hm[num];
        }
        priority_queue <int> counts;
        for (auto it : hm) {
            counts.push(it.second);
        }

        int target = (arr.size() + 1) / 2;
        int res = 0;
        while (!counts.empty()) {
            int tmp = counts.top();
            counts.pop();
            target -= tmp;
            ++res;
            if (target <= 0) return res;
        }
        return res;
    }
};


class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> hm;
        for (auto num : arr) {
            ++hm[num];
        }
        
        vector<int> counts;
        for (auto it : hm) {
            counts.push_back(it.second);
        }
        sort(counts.begin(), counts.end());
        reverse(counts.rbegin(), counts.rend());

        int target = (arr.size() + 1) / 2;
        int res = 0;
        for (auto cnt : counts) {
            target -= cnt;
            ++res;
            if (target <= 0) return res;
        }
        return res;
    }
};