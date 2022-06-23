#include<vector>
#include<algorithm>
#include<queue>
#include<iostream>

using namespace std;
class Solution {
public:
    static bool compare(vector<int>& m, vector<int>& n){
        return m[1]<n[1];
    }
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(), courses.end(), compare);
        priority_queue<int> heap;
        int curr_days = 0;
        for(vector<int> course: courses){
            if(curr_days+course[0] <= course[1]){
                curr_days += course[0];
                heap.push(course[0]);
            }else if(!heap.empty() && heap.top()>course[0]){
                curr_days = curr_days - heap.top() + course[0];
                heap.pop();
                heap.push(course[0]);
            }
        }
        return heap.size();
    }
};

int main(){
    Solution sol;
    vector<vector<int>> courses = {{3,2},{4,3}};
    // cout<<sol.compare(courses)<<endl;
}