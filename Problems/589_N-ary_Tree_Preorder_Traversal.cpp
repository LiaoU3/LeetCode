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
    vector<int>res;
    vector<int> preorder(Node* root) {
        traverse(root);
        return res;
    }
private:
    void traverse(Node* node){
        if(!node) return;
        res.push_back(node->val);
        for(auto child: node->children)
            traverse(child);
    }
};