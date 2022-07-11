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