#include <stack>
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

class Solution {
public:
    int kthSmallest(TreeNode* root, int &k) {
        if(!root) return -1;
        int res = kthSmallest(root->left, k);
        if(res!=-1) return res;
        k--;
        if(k==0) return root->val;
        return kthSmallest(root->right, k); 
    }
};

class Solution {
public:
    int K;
    int kthSmallest(TreeNode* root, int k) {
        K = k;
        return traverse(root);
    }
    int traverse(TreeNode* node){
        if(!node) return -1;
        int res = traverse(node->left);
        if(res!=-1) return res;
        K--;
        if(K==0) return node->val;
        return traverse(node->right);
    }
};

class Solution {
public:
    int count;
    int kthSmallest(TreeNode* root, int k){
        stack<TreeNode*> st;
        st.push(root);
        TreeNode* curr = root;
        while(!st.empty() || curr){
            while(curr){
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            k--;
            if(k==0){
                return curr->val;
            }
            curr = curr->right;
        }
        return -1;
    }
};