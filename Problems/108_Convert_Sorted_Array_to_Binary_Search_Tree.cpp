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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums, 0, nums.size()-1);
    }
    TreeNode* build(vector<int>& nums, int left, int right) {
        if (left > right) return nullptr;
        int middle = (left+right) / 2;
        TreeNode* father = new TreeNode(nums[middle]);
        father -> left = build(nums, left, middle-1);
        father -> right = build(nums, middle+1, right);
        return father;
    }
};

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return convert(nums, 0, nums.size()-1);
    }
    
    TreeNode* convert(vector<int>& nums, int left, int right){
        if(left==right){
            return new TreeNode(nums[left]);
        }
        if(left>right){
            return nullptr;
        }
        int middle = (left+right)/2;
        TreeNode* node = new TreeNode(nums[middle]);
        node->left = convert(nums, left, middle-1);
        node->right = convert(nums, middle+1, right);
        return node;
    }
};