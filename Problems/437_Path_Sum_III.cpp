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


// TLE
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        int cnt = 0;
        // presum, count
        unordered_map<long long, int> tmp;
        tmp[0] = 1;
        traverse(root, cnt, 0, tmp, targetSum);
        return cnt;
    }
    void traverse(TreeNode* node, int &cnt, long long currSum, unordered_map<long long, int>preSums, int targetSum){
        if(!node) return;
        currSum += node->val;
        cnt += preSums[currSum-targetSum];
        preSums[currSum]++;

        traverse(node->left,  cnt, currSum, preSums, targetSum);
        traverse(node->right, cnt, currSum, preSums, targetSum);
    }
};