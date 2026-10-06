# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def dfs(curr):
            if not curr:
                return 0
            
            l_height = dfs(curr.left)
            r_height = dfs(curr.right)

            if abs(l_height - r_height) > 1:
                self.is_balanced = False

            return 1 + max(l_height, r_height)
        
        dfs(root)
        return self.is_balanced