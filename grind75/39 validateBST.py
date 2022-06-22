# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValid(root, range):
            if not root:
                return True
            
            elif not (range[0] < root.val < range[1]):
                return False
            
            return isValid(root.left, (range[0], root.val)) and isValid(root.right, (root.val, range[1]))
        
        return isValid(root.left, (-sys.maxsize, root.val)) and isValid(root.right, (root.val, sys.maxsize))
        
        