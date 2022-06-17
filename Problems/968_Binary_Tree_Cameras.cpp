#include<iostream>

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
    int camera_count = 0;
    int minCameraCover(TreeNode* root) {
        if (traverse(root)){
            return camera_count;
        }else{
            return camera_count+1;
        }
    }
    // None: 0, Covered: 1, Camera: 2
    int traverse(TreeNode* node){
        if (! node){
            return 1;
        }
        int l = traverse(node->left);
        int r = traverse(node->right);
        if (l==0 || r==0){
            camera_count++;
            return 2;
        }
        if (l==2 || r==2){
            return 1;
        }
        return 0;
    }
};