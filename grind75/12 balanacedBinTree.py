# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from tabnanny import check
from turtle import right
from typing import Optional


class Solution:
    ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkBalance(node):
            if not self.ans:
                return 0
            if not node:
                return 0
            
            lDepth = checkBalance(node.left)
            rDepth = checkBalance(node.right)

            if abs(lDepth - rDepth) > 1:
                self.ans = False
            return 1 + max(lDepth, rDepth)
        
        checkBalance(root)
        return self.ans