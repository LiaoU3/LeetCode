class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        int maxHorizontal = horizontalCuts[0];
        for(int i=1; i<horizontalCuts.size(); i++){
            maxHorizontal = max(maxHorizontal, horizontalCuts[i]-horizontalCuts[i-1]);
        }
        maxHorizontal = max(maxHorizontal, h-horizontalCuts[horizontalCuts.size()-1]);
        int maxVertical   = verticalCuts[0];
        for(int i=1; i<verticalCuts.size(); i++){
            maxVertical = max(maxVertical, verticalCuts[i]-verticalCuts[i-1]);
        }
        maxVertical = max(maxVertical, w-verticalCuts[verticalCuts.size()-1]);
    return (int)((long) maxHorizontal*maxVertical%1000000007);
    }
};