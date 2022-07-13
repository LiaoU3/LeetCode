class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> stackS, stackT;
        for(auto c: s){
            if(c=='#'){
                if(stackS.size())stackS.pop();
            }else{
                stackS.push(c);
            }
        }
        for(auto c: t){
            if(c=='#'){
                if(stackT.size())stackT.pop();
            }else{
                stackT.push(c);
            }
        }
        return stackS==stackT;
    }
};