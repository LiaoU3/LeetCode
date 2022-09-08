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
    string tree2str(TreeNode* root) {
        string res = traverse(root);
        return res;
    }
    string traverse(TreeNode* node) {
        string s;
        if (!node) return s;
        string l = traverse(node -> left);
        string r = traverse(node -> right);
        s = to_string(node -> val);
        if (!l.length() && !r.length()) {
            return s;
        } else if (!l.length()) {
            return s + "()" + '(' + r + ')';
        } else if (! r.length()) {
            return s + '(' + l + ')';
        } else {
            return s + '(' + l + ')' + '(' + r + ')';
        }
    }
};