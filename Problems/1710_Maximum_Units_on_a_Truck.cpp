class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](auto& box1, auto& box2) {
            return box1[1] > box2[1];
        });
        int unitCount = 0;
        for(int i=0; i<boxTypes.size(); i++){
            if(boxTypes[i][0]<truckSize){
                unitCount += boxTypes[i][0]*boxTypes[i][1];
                truckSize -= boxTypes[i][0];
            }else{
                unitCount += truckSize*boxTypes[i][1];
                break;
            }
        }
        return unitCount;
    }
};