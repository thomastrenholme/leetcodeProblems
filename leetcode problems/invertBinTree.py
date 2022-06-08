# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root or (not root.left and not root.right):
            return root

        
        def invert(node):


            if node.left and node.right:
                temp = node.left
                node.left = node.right
                node.right = temp
                invert(node.left)
                invert(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                invert(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                invert(node.left)
        invert(root)

        return root

g = Solution
            
        