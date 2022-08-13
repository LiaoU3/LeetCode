#include<iostream>
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

// class Solution {
// public:
//     int diameterOfBinaryTree(TreeNode* root) {
//         int maxLen = 0;
//         depth(root, maxLen);
//         return maxLen;
//     }

//     int depth(TreeNode* root, int &maxLen){
//         if(!root) return 0;
//         int left = depth(root->left, maxLen);
//         int right = depth(root->right, maxLen);
//         maxLen = max(maxLen, left+right);
//         return max(left, right)+1;
//     }
// };

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int longest = 0;
        traverse(root, longest);
        return longest;
    }
    int traverse(TreeNode* node, int& longest) {
        if (!node) return 0;
        int l = traverse(node -> left, longest);
        int r = traverse(node -> right, longest);
        longest = max(longest, l+r);
        return max(l, r) + 1;
    }
};

class Solution {
public:
	int maxLen = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return maxLen;
    }

    int depth(TreeNode* root){
        if(!root) return 0;
        int left = depth(root->left);
        int right = depth(root->right);
        maxLen = max(maxLen, left+right);
        return max(left, right)+1;
    }
};

