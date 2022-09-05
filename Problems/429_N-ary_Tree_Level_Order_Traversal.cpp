/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<Node*> qu;
        qu.push(root);
        while (!qu.empty()) {
            int len = qu.size();
            vector<int> tmp;
            for (int i = 0; i < len; ++i) {
                Node* curr = qu.front();
                qu.pop();
                tmp.push_back(curr -> val);
                for (const auto &node : curr -> children) {
                    qu.push(node);
                }
            }
            res.push_back(tmp);
        }
        return res;
    }
};