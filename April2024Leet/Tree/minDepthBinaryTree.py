import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.min = sys.maxsize

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dig(root, 1)

        return self.min

    def dig(self, root, ctr):

        if root is None or ctr > self.min:
            return

        if root.left is None and root.right is None:
            if ctr < self.min:
                self.min = ctr
        else:
            self.dig(root.left, ctr+1)
            self.dig(root.right, ctr+1)
