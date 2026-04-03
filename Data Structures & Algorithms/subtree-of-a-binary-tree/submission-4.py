# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findEqualRoot(curr, subRoot):
            if not curr:
                return False
            if checkSubtree(curr, subRoot):
                return True
            return (findEqualRoot(curr.left, subRoot) or findEqualRoot(curr.right, subRoot))
        
        def checkSubtree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            print(p.val, q.val)

            val_equal = p.val == q.val
            left_equal = checkSubtree(p.left, q.left)
            right_equal = checkSubtree(p.right, q.right)

            return val_equal and left_equal and right_equal
        
        return findEqualRoot(root, subRoot)