# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(root, path):
            path = (path << 1) + root.val
            if not root.left and not root.right:
                self.answer += path
            else:
                if root.left:
                    dfs(root.left, path)
                if root.right:
                    dfs(root.right, path)
        
        dfs(root, 0)
        return self.answer
