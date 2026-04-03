# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            left_length = helper(node.left) + 1
            right_length = helper(node.right) + 1
            return max(left_length, right_length)

        return helper(root)