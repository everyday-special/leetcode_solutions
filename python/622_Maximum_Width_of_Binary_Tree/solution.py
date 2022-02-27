# Written after checking the discussion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(0, root)])
        answer = 0
        while q:
            temp = []
            for _ in range(len(q)):
                i, node = q.popleft()
                temp.append(i)
                if node.left:
                    q.append((i * 2 + 1, node.left))
                if node.right:
                    q.append((i * 2 + 2, node.right))
            answer = max(answer, max(temp) - min(temp) + 1)
        return answer
