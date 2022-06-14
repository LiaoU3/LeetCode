#include<iostream>
#include<vector>
#include<map>
#include<set>

using namespace std;

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        map<int, set<int>> graph;
        for(auto connect: connections){
            graph[connect[0]].insert(connect[1]);
            graph[connect[1]].insert(connect[0]);
        }
        
    }
};