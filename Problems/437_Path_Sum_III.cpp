#include <unordered_map>
#include<vector>
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

// pass by reference makes it faster
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        int cnt = 0;
        // {pastSum, count}
        unordered_map<long long, int> seen;
        seen[0] = 1;
        traverse(root, targetSum, seen, cnt, 0);
        return cnt;
    }
    void traverse(TreeNode* node, int targetSum, unordered_map<long long, int>& seen, int& cnt, long long currSum) {
        if (!node) return;
        currSum += node -> val;
        cnt += seen[currSum - targetSum];
        ++seen[currSum];
        traverse(node -> left, targetSum, seen, cnt, currSum);
        traverse(node -> right, targetSum, seen, cnt, currSum);
        --seen[currSum];
    }
};

// Only faster than 5% of submissions
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        int cnt = 0;
        // {pastSum, count}
        unordered_map<long long, int> seen;
        seen[0] = 1;
        traverse(root, targetSum, seen, cnt, 0);
        return cnt;
    }
    void traverse(TreeNode* node, int targetSum, unordered_map<long long, int> seen, int& cnt, long long currSum) {
        if (!node) return;
        currSum += node -> val;
        cnt += seen[currSum - targetSum];
        ++seen[currSum];
        traverse(node -> left, targetSum, seen, cnt, currSum);
        traverse(node -> right, targetSum, seen, cnt, currSum);
    }
};

class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        int cnt = 0;
        vector<long> tmp = {0};
        traverse(root, targetSum, tmp, cnt);
        return cnt;
    }
    void traverse(TreeNode* node, int targetSum, vector<long> seen, int& cnt) {
        if (!node) return;
        long currSum = seen[seen.size()-1] + node -> val;
        for (long num : seen) {
            if (currSum - num == targetSum)
                ++cnt;
        }
        seen.push_back(currSum);
        traverse(node -> left, targetSum, seen, cnt);
        traverse(node -> right, targetSum, seen, cnt);
    }
};


// TLE
// class Solution {
// public:
//     int pathSum(TreeNode* root, int targetSum) {
//         int cnt = 0;
//         // presum, count
//         unordered_map<long long, int> tmp;
//         tmp[0] = 1;
//         traverse(root, cnt, 0, tmp, targetSum);
//         return cnt;
//     }
//     void traverse(TreeNode* node, int &cnt, long long currSum, unordered_map<long long, int>preSums, int targetSum){
//         if(!node) return;
//         currSum += node->val;
//         cnt += preSums[currSum-targetSum];
//         preSums[currSum]++;

//         traverse(node->left,  cnt, currSum, preSums, targetSum);
//         traverse(node->right, cnt, currSum, preSums, targetSum);
//     }
// };