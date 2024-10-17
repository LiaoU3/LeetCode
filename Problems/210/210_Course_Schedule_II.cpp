#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    unordered_map<int, vector<int>> graph;
    vector<int> res;
    vector<int> status;
    bool isPossible = true;
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i = 0; i < numCourses; ++i) {
            status.push_back(0);
        }

        for (vector<int> courses : prerequisites) {
            graph[courses[0]].push_back(courses[1]);
        }

        for (int i = 0; i < numCourses; ++i) {
            if (status[i] == 0) {
                dfs(i);
            }
        }

        if (isPossible) {
            return res;
        } else {
            vector<int> tmp;
            return tmp;
        }
    }

    void dfs(int course) {
        if (!isPossible) return;
        status[course] = 1;
        for (int request : graph[course]) {
            if (status[request] == 0) {
                dfs(request);
            } else if (status[request] == 1) {
                isPossible = false;
                return;
            }
        }
        status[course] = 2;
        res.push_back(course);
    }
};