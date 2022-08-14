#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <iostream>
using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;
        unordered_map<int, vector<int>> hm;
        for (int i = 0; i < routes.size(); ++i) {
            vector<int> route(routes[i]);
            for (auto stop : route) {
                hm[stop].push_back(i);
            }
        }
        // 0 : unused, 1 : used
        vector<int> routeStatus(routes.size(), 0);
        queue<int> qu;
        qu.push(source);
        int cnt = 0;
        while (!qu.empty()) {
            int len = qu.size();
            ++cnt;
            for (int i = 0; i < len; ++i) {
                int currStop = qu.front();
                qu.pop();
                for (auto route : hm[currStop]) {
                    if (routeStatus[route]) {
                        continue;
                    }
                    routeStatus[route] = 1;
                    for (auto otherStop : routes[route]) {
                        if (otherStop == target) {
                            return cnt;
                        }
                        qu.push(otherStop);
                    }
                }
            }
        }
        return -1;
    }
};

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;
        // int : stop, set<int> : every busNum pass through this stop
        unordered_map<int, unordered_set<int>> busStop;

        for (int i = 0; i < routes.size(); ++i) {
            for (int stop : routes[i]) {
                busStop[stop].insert(i);
            }
        }
        unordered_set<int> usedBus;
        queue<int> qu;
        qu.push(source);
        int cnt = 0;
        while (!qu.empty()) {
            int length = qu.size();
            ++cnt;
            for (int i = 0; i < length; ++i) {
                int curr = qu.front();
                qu.pop();
                for (int bus : busStop[curr]) {
                    if (usedBus.count(bus)) continue;
                    usedBus.insert(bus);
                    for (auto stop : routes[bus]) {
                        if (stop == target) return cnt;
                        qu.push(stop);
                    }
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> routes = {{1,2,7},{3,6,7}};
    int source = 1;
    int target = 6;
    cout << sol.numBusesToDestination(routes, source, target);
}