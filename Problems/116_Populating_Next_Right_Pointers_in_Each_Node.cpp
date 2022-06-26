#include<queue>
#include<stdlib.h>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};


class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*> qu;
        qu.push(root);
        while(!qu.empty()){
            int qu_len = qu.size();
            for(int i=0; i<qu_len; i++){
                Node* curr = qu.front();
                qu.pop();
                if(i<qu_len-1) curr->next = qu.front();
                if(curr->left) qu.push(curr->left);
                if(curr->right)qu.push(curr->right);
            }
        }
        return root;
    }
};