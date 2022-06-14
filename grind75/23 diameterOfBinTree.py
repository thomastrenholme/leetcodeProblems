# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    maxDiameter=0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ##go through each node, dfs left and right of the node. add together, if greater than greatest diameter, switch diameter to that val

        def dfsTree(node, currDepth):
            if node:
                lD = dfsTree(node.left, 1) if node.left else 0
                rD = dfsTree(node.right, 1) if node.right else 0
                d = lD+rD
                self.maxDiameter=max(d, self.maxDiameter)
                return 1 + max(lD, rD)
            else:
                return currDepth


        
        dfsTree(root, 0)
        return self.maxDiameter