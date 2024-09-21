# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Checking if both nodes are null or not
        if not p and not q:
            return True

        # Checking if one of the node is null or not 
        # Checking if both the values are same or not
        if not p or not q or p.val != q.val:
            return False

        ''' Recursively passing both (right, left) node to "isSameTree()" function & return the "True/False" '''
          
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))