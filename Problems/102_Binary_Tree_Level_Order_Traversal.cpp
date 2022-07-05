#include<vector>
#include<queue>

using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root) return res;
        queue<TreeNode*> qu;
        qu.push(root);
        while(!qu.empty()){
            int length = qu.size();
            vector<int> tmp;
            for(int i=0; i<length; i++){
                TreeNode* node = qu.front();
                tmp.push_back(node->val);
                qu.pop();
                if(node->left) qu.push(node->left);
                if(node->right) qu.push(node->right);
            }
            res.push_back(tmp);
        }
        return res;
    }
};
