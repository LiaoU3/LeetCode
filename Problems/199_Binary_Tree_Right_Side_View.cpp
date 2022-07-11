#include<vector>
#include<queue>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace std;

// dfs
class Solution {
public:
    vector<int> rightView;
    vector<int> rightSideView(TreeNode* root) {
        traverse(root, 0);
        return rightView;
    }
    void traverse(TreeNode* node, int height){
        if(node==NULL) return;
        if(height==rightView.size()) rightView.push_back(node->val);
        traverse(node->right, height+1);
        traverse(node->left, height+1);
    }
};

// bfs
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> rightView;
        if(!root) return rightView;
        queue<TreeNode*> qu;
        qu.push(root);
        while(!qu.empty()){
            int length = qu.size();
            rightView.push_back(qu.back()->val);
            for(int i=0; i<length; i++){
                TreeNode* node = qu.front();
                qu.pop();
                if(node->left != NULL) qu.push(node->left);
                if(node->right != NULL) qu.push(node->right);
            }
        }
        return rightView;
    }
};