/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(!root) return true;
        int left = depth(root->left);
        int right = depth(root->right);
        if(right-left>1 || right-left<-1) return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }
    int depth(TreeNode* root){
        if(!root) return 0;
        int left = depth(root->left);
        int right = depth(root->right);
        return max(left, right)+1;
    }
};