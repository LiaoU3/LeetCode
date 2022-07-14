class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(auto stone: stones)pq.push(stone);
        while(pq.size()>1){
            int heaviest = pq.top();
            pq.pop();
            int second = pq.top();
            pq.pop();
            if(heaviest!=second)pq.push(heaviest-second);
        }
        if(pq.size()){
            return pq.top();
        }else{
            return 0;
        }
    }
};