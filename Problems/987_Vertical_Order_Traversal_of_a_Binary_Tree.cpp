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
    map<int, vector<pair<int, int>>> hm;
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        dfs(root, 0, 0);
        vector<vector<int>> res;
        for (auto it : hm) {
            sort(it.second.begin(), it.second.end());
            vector<int> tmp;
            for (auto i : it.second) {
                tmp.push_back(i.second);
            }
            res.push_back(tmp);
        }
        return res;
    }
    void dfs(TreeNode* node, int level, int order) {
        if (! node) return;
        hm[order].push_back({level, node -> val});
        dfs(node -> left,  level + 1, order - 1);
        dfs(node -> right, level + 1, order + 1);
    }
};

