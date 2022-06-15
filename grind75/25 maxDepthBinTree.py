# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maximumDepth=0
    visited = {}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def dfsTree(node, currDepth):

            if not node.left and not node.right:
                self.maximumDepth = max(self.maximumDepth, currDepth)
                return
            
            elif not node.right:
                dfsTree(node.left, currDepth+1)
            elif not node.left:
                dfsTree(node.right, currDepth+1)
            else:
                ##right and left
                dfsTree(node.left, currDepth+1)
                dfsTree(node.right, currDepth+1)
        dfsTree(root, 1)
        return self.maximumDepth