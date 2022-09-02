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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        queue<TreeNode*> qu;
        qu.push(root);
        while (!qu.empty()) {
            int len = qu.size();
            double total = 0;
            for (int i = 0; i < len; ++i) {
                TreeNode* node = qu.front();
                qu.pop();
                total += node -> val;
                if (node -> left) {
                    qu.push(node -> left);
                }
                if (node -> right) {
                    qu.push(node -> right);
                }
            }
            res.push_back(total / len);
        }
        return res;
    }
};