#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> graph(n);
        for(auto connect: connections){
            if (find(graph[connect[0]].begin(), graph[connect[0]].end(), connect[1]) == graph[connect[0]].end()) {
                graph[connect[0]].push_back(connect[1]);
            }
            if (find(graph[connect[1]].begin(), graph[connect[1]].end(), connect[0]) == graph[connect[1]].end()) {
                graph[connect[1]].push_back(connect[0]);
            }
        }
        vector<int> min_step_list(n, -1);
        vector<vector<int>> res;
        dfs(0, -1, 0, min_step_list, graph, res);
        return res;
    }

    int dfs(int curr, int parent, int curr_step, vector<int>& min_step_list, vector<vector<int>>&graph, vector<vector<int>> &res){

        min_step_list[curr] = curr_step+1;
        for(auto child: graph[curr]){
            if (child == parent){
                continue;
            }
            if(min_step_list[child] == -1){    
                min_step_list[curr] = min(min_step_list[curr], dfs(child, curr, curr_step+1, min_step_list, graph, res));
            }else{
                min_step_list[curr] = min(min_step_list[curr], min_step_list[child]);
            }
        }

        if(min_step_list[curr] == curr_step+1 && curr!=0){
            vector<int> temp;
            temp.push_back(curr);
            temp.push_back(parent);
            res.push_back(temp);
        }
        return min_step_list[curr];
    }
};