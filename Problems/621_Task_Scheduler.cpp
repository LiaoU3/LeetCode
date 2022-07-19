class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int>taskCnt(26, 0);
        for(char c: tasks){
            taskCnt[c-'A']++;
        }
        int maxCnt = 0;
        int maxCntTaskCnt = 0;
        for(int cnt: taskCnt){
            if(cnt>maxCnt){
                maxCnt = cnt;
                maxCntTaskCnt = 1;
            }else if(cnt==maxCnt){
                maxCntTaskCnt++;
            }
        }
        int ans = (maxCnt-1)*(n+1) + maxCntTaskCnt;
        return ans>tasks.size()?ans:tasks.size();
    }
};