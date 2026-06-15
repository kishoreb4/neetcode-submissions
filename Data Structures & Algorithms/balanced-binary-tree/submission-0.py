# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                return 0  # height of empty tree is 0

            left = dfs(node.left)
            right = dfs(node.right)

            # If either child is already unbalanced, propagate failure up
            if left == -1 or right == -1:
                return -1

            # If current node is unbalanced, signal failure
            if abs(left - right) > 1:
                return -1

            # Otherwise return height as normal
            return 1 + max(left, right)

        return dfs(root) != -1        