class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        unordered_set<int> numsSet(nums.begin(), nums.end());
        int longest = 1;
        for(auto num: numsSet){
            // which means it's the start of the sequence
            if(!numsSet.count(num-1)){
                int length = 1;
                while(numsSet.count(num+1)){
                    length++;
                    num++;
                    longest = max(longest, length);
                }
            }
        }
        return longest;
    }
};