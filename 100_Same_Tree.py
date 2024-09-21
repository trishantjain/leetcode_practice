# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    DESCRIPTION: 

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


'''
class Solution:
    def isSameTree(self, p, q) -> bool:
        # Checking if both nodes are null or not
        if not p and not q:
            return True

        # Checking if one of the node is null or not 
        # Checking if both the values are same or not
        if not p or not q or p.val != q.val:
            return False

        ''' Recursively passing both (right, left) node to "isSameTree()" function & return the "True/False" '''
          
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))