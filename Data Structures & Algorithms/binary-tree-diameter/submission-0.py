# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(curr):
            if not curr:
                return 0

            l_height = dfs(curr.left)
            r_height = dfs(curr.right)
            diameter = l_height + r_height

            if diameter > self.max_diameter:
                self.max_diameter = diameter
            
            return 1 + max(l_height, r_height)
        
        dfs(root)
        return self.max_diameter