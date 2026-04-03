# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, lower_limit, upper_limit):
            if not curr:
                return True

            if not (curr.val > lower_limit and curr.val < upper_limit):
                return False

            valid_bst_left = dfs(curr.left, lower_limit, min(upper_limit, curr.val))
            valid_bst_right = dfs(curr.right, max(lower_limit, curr.val), upper_limit)

            return valid_bst_left and valid_bst_right
        return dfs(root, -math.inf, math.inf)

