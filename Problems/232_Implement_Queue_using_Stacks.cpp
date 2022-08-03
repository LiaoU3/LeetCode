class MyQueue {
public:
    stack<int> stck1;
    stack<int> stck2;
    
    MyQueue() {
        
    }
    
    void push(int x) {
        while (!stck2.empty()) {
            stck1.push(stck2.top());
            stck2.pop();
        }
        stck1.push(x);
    }
    
    int pop() {
        while (!stck1.empty()) {
            stck2.push(stck1.top());
            stck1.pop();
        }
        int res = stck2.top();
        stck2.pop();
        return res;
    }
    
    int peek() {
        while (!stck1.empty()) {
            stck2.push(stck1.top());
            stck1.pop();
        }
        return stck2.top();
    }
    
    bool empty() {
        return stck1.empty() && stck2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */