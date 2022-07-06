class Solution {
public:
    int fib(int n) {
        int pre = 1;
        int prepre = 0;
        if(n==0) return prepre;
        if(n==1) return pre;
        int curr;
        for(int i=0; i<n-1; i++){
            curr = pre+prepre;
            prepre = pre;
            pre = curr;
        }
        return curr;
    }
};