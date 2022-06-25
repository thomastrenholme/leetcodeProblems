# Definition for a binary tree node.
from tabnanny import check


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ##If q or p not found, return None, else return the p or q node
        if not root or root == q or root == p:
            return root
        
        ##Check if the left and right nodes hold p or q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        ##if both, return both
        if l and r:
            return root
        
        ##If not the LCA, return the found node (either l or r)
        return l if l else r