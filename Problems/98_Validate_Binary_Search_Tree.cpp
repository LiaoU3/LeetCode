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

// cleanest solution
class Solution {
public:
    bool isValidBST(TreeNode* root, long lowerBound = LONG_MIN, long upperBound = LONG_MAX) {
        if (!root) return false;
        if (root -> val > upperBound || lowerBound > root -> val) return false;
        return isValidBST(root -> left, lowerBound, root -> val) && isValidBST(root -> right, root -> val, upperBound);
    }
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return traverse(root,LONG_MIN,LONG_MAX);
    }
    bool traverse(TreeNode* node, long long minVal, long long maxVal){
        if(node==nullptr) return true;
        if(node->val >= maxVal || node->val <= minVal)return false;
        return traverse(node->left, minVal, node->val) && traverse(node->right, node->val, maxVal);
    }
};