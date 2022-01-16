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
    int sumRootToLeaf(TreeNode* root) {
        this->answer = 0;
        this->dfs(root, 0);
        return this->answer;
    }
private:
    int answer;
    void dfs(TreeNode* root, int path) {
        path = (path << 1) + root->val;
        if (!root->left && !root->right)
            this->answer += path;
        else
        {
            if (root->left)
                dfs(root->left, path);
            if (root->right)
                dfs(root->right, path);
        }
    }
};
