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
    int goodNodes(TreeNode* root) {
        int cnt = 0;
        traverse(root, INT_MIN, cnt);
        return cnt;
    }
    void traverse(TreeNode* node, int seenBig, int &cnt) {
        if (!node) return;
        if (node -> val >= seenBig) {
            ++cnt;
        }
        seenBig = max(seenBig, node -> val);
        traverse(node -> left, seenBig, cnt);
        traverse(node -> right, seenBig, cnt);
    }
};