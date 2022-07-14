class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string,int> hashMap;
        priority_queue<pair<int, string>> pq;
        for(auto word: words) hashMap[word]++;
        for(auto el: hashMap){
            pq.push({-el.second, el.first});
            if(pq.size()>k) pq.pop();
        }
        vector<string> ans;
        while(!pq.empty()){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        
        reverse(ans.begin(),ans.end());
        return ans;
    }
};