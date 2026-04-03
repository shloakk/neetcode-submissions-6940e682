# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            val_equal = p.val == q.val
            left_equal = helper(p.left, q.left)
            right_equal = helper(p.right, q.right)

            return val_equal and left_equal and right_equal
        
        return helper(p, q)